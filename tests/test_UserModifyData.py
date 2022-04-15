import sys
import random
import string
sys.path.append("..")
from src.User import User
from tests.assertion_errors import assertion_error_messages as ae

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