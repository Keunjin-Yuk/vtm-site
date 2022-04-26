import app

def test_estimate():
    """ 
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    print("\r")
    print(" -- calculate_current_age unit test")
    assert app.estimate(180,360) == 141300.0  #will change as the years progress
