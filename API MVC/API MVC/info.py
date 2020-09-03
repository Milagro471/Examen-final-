import json as JSON 
import os, sys
from model import User

class DataHandlerUser:

    def __init__(self):
        self.list_users = self.load_users()

    def load_file(self):
        with open('datos.json', 'r') as file:
            data = file.read()
            json_data = JSON.load(data)
        return json_data

    