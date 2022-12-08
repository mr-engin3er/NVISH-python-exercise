from src.app import create_app

def test_create_app():
    app = create_app("test")
    assert app.config.get("TESTING") == True , f'Expecting testing in config to be {True} but got {app.config.get("TESTING")}'