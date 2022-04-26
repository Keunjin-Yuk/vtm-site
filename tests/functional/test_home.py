import time

def test_index(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Welcome to VTM" in res.data
        


def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/mike' route is requested (GET)
    THEN check that the response is valid
    """
    print("-- /about GET test")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About VTM" in res.data

  
def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/age' route is requested (GET)
    THEN check that the correct page is displayed
    """
    print("-- /estimate GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Radius:" in res.data
        assert b"Height:" in res.data
