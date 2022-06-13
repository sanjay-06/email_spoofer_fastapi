
from db import user
import bcrypt

class Auth:

    @staticmethod
    def checkuser(username,password):

        print(username)
        userquery=user.find_one({"username":username})
        print(userquery)

        if userquery:
            passenc=bcrypt.hashpw(password.encode('utf-8'), userquery['salt'])
            if(userquery['password'] == passenc):
                return True
        return False

