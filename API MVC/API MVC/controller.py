
from model import User
from extractor import Extractor
from app import *
import os, sys

class ControllerUser:
    def __init__(self):
        self.Users = Users()
        self.extractor = Extractor()
        self.list_User = self.extractor.extractorUsers

    def loadUser(self, log_data):
        username = log_data['User']
        password = log_data['Pass']
        for User in self.list_User:
            if username == Users.User:
                if str(password) == Users.Pass
                    return Users
                else:
                    return jsonify({"'Invalid Credentials. Please try again.'"})
    