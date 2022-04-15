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

# COMMENTED OUT "test_signUp()" TO REDUCE NEW USER DOCUMENTS IN THE DATABASE 

# def test_signUp():
# # initialize a User object
#     temp_user = User()
#     # assert that the user is not signed in
#     assert temp_user.signed_in == False, ae["uso"]
#     #sign in with correct credentials
#     temp_user.signUp("bionicle@lego.com","thegoldenmask","Joe","Bio")
    
#     # validate that user exists in db and assert that they can sign-in
#     assert temp_user.validateUserLogin("bionicle@lego.com","thegoldenmask") == True, ae["uso"]
    