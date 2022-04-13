import sys
import random
import string
sys.path.append("..")
from src.User import User
from tests.assertion_errors import assertion_error_messages as ae
def test_userCreation():
    # initialize a User object
    temp_user = User()
    # assert that the user is not signed in
    assert temp_user.signed_in == False, ae["uso"]

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


def test_UserCorrectSignIn():
    # initialize a User object
    temp_user = User()
    # assert that the user is not signed in
    assert temp_user.signed_in == False, ae["uso"]
    #sign in with correct credentials
    if(temp_user.validateUserLogin("eldenlord@souls.net","moonviel")):
        print("test_user correct sign-in successful, EXPECTED")
        assert temp_user.signed_in == True, ae["usi"]
    else:
        print("test_user correct sign-in, UNEXPECTED")
        assert temp_user.signed_in == False, ae["usi"]


# def test_signUp():
# # initialize a User object
#     temp_user = User()
#     # assert that the user is not signed in
#     assert temp_user.signed_in == False, ae["uso"]
#     #sign in with correct credentials
#     temp_user.signUp("bionicle@lego.com","thegoldenmask","Joe","Bio")
    
#     # validate that user exists in db and assert that they can sign-in
#     assert temp_user.validateUserLogin("bionicle@lego.com","thegoldenmask") == True, ae["uso"]
    

def test_changeUserData():
# initialize a User object
    temp_user = User()
#   assert that user is signed out
    assert temp_user.signed_in == False, ae["uso"]
#   sign in a specific user
    assert temp_user.validateUserLogin("bionicle@lego.com","thegoldenmask") == True, ae["uso"]
#   modify first name field
    random_string = ''.join(random.choices(string.ascii_lowercase,k=5))
    temp_user.changeUserData("first_name",random_string)
    
#   assert that the value was changed in the DB
    assert temp_user.getUserField("first_name") == random_string, ae["wfv"]
