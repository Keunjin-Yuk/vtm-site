import app

def test_area():
    """ 
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    print("\r")
    print(" -- calculate_current_age unit test")
    assert app.area(180,360) == 3532.5  

def test_cost():
    """ 
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    print("\r")
    print(" -- calculate_current_age unit test")
    assert app.cost(3532.5) == 141300.0