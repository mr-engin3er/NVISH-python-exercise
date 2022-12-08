from flask import request, Blueprint
from .utils import get_db_connection
from .redis_utils import is_redis_connected, set_dict,get_dict, delete_cache


exercise3 = Blueprint("exercise3", __name__)


@exercise3.route("/save", methods=["POST"])
def save_post():
    title = request.json.get("title")
    content = request.json.get("content")
    if not title or not content:
        return {"error": "title and content are required."}, 400

    connection = get_db_connection()
    cur = connection.cursor()
    try:
        cur.execute("INSERT into post (title, content) VALUES (?, ?)",
                    (title, content)
                    )
        connection.commit()
        connection.close()
        if is_redis_connected():
            delete_cache("post-all")
        return {"message": "post saved successfully"}, 201
    except Exception as err:
        connection.close()
        return {"error": f"error in saving post, {str(err)}"}, 500


@exercise3.route("/get", methods=["GET"])
@exercise3.route("/get/<post_id>", methods=["GET"])
def get_post(post_id=None):
    connection = get_db_connection()
    cur = connection.cursor()
    try:
        if post_id:
            if is_redis_connected():
                cache = get_dict(f"post-{post_id}")
                if cache:
                    return {"data": cache}, 200
            cur.execute(f"SELECT * from post where id = '{post_id}';")
            post = cur.fetchone()
            connection.close()
            if post:
                if is_redis_connected():
                    print("post",post)
                    set_dict(f"post-{post_id}",post)
                return {"data": post}, 200
            return {"error": f"post not found with id {post_id}"}, 404
        if is_redis_connected():
            cache = get_dict("post-all")
            if cache:
                return {"data": cache}, 200
        cur.execute("SELECT * from post;")
        posts = cur.fetchall()
        connection.close()
        if posts and is_redis_connected():
            set_dict("post-all",posts)
        return {"data": posts}, 200
    except Exception as err:
        print(err)
        connection.close()
        return {"error": "Internal server error"}, 500


@exercise3.route("/delete", methods=["DELETE"])
@exercise3.route("/delete/<post_id>", methods=["DELETE"])
def delete_post(post_id=None):
    connection = get_db_connection()
    cur = connection.cursor()
    try:
        if post_id:
            cur.execute(f"SELECT * from post where id = '{post_id}';")
            post = cur.fetchone()
            if post:
                cur.execute(f"DELETE from post where id = '{post_id}';")
                connection.commit()
                connection.close()
                if is_redis_connected():
                    delete_cache(f"post-{post_id}")
                    delete_cache("post-all")
                return {"message": f"Post deleted successfully with id {post_id}"}, 200
            return {"error": f"post not found with id {post_id}"}, 404

        cur.execute("DELETE from post;")
        connection.commit()
        connection.close()
        if is_redis_connected():
            delete_cache("post-all")
        return {"message": "All posts deleted successfully."}, 200
    except Exception as err:
        print(err)
        connection.close()
        return {"error": "Internal server error"}, 500
