from info import DataHandlerUser
from model import User

class Extractor:
    def __init__(self):
        self.extractorUsers = ExtractUsers_Info()

class ExtractUsers_Info:
    def __init__(self):
        self.existing_users = DataHandlerUser().list_users
        