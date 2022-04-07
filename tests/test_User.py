import sys
sys.path.append("..")
from src.User import User
from tests.assertion_errors import assertion_error_messages as ae
def test_userCreation():
    # initialize a User object
    temp_user = User()
    # assert that the user is not signed in
    assert temp_user.signed_in == False, ae["uso"]
    return True

def test_UserIncorrectSignIn():
    # initialize a User object
    temp_user = User()
    # assert that the user is not signed in
    assert temp_user.signed_in == False, ae["uso"]
    #sign in with incorrect credentials
    if(temp_user.validateUserLogin("planting_seeds@usa.net","anongus")):
        print("test_user incorrect sign-in successful, UNEXPECTED")
        assert temp_user.signed_in == False, ae["uso"] 
    else:
        print("test_user incorrect sign-in failure, EXPECTED")
        assert temp_user.signed_in == False, ae["uso"]
    
    return True

def test_UserCorrectSignIn():
    # initialize a User object
    temp_user = User()
    # assert that the user is not signed in
    assert temp_user.signed_in == False, ae["uso"]
    #sign in with incorrect credentials
    if(temp_user.validateUserLogin("s_higley@u.pacific.edu","toothpaste")):
        print("test_user correct sign-in successful, EXPECTED")
        assert temp_user.signed_in == True, ae["usi"]
    else:
        print("test_user correct sign-in, UNEXPECTED")
        assert temp_user.signed_in == False, ae["usi"]
    
    return True
test_UserIncorrectSignIn()
test_UserCorrectSignIn()