import base64
from .base_prac import Auth

class BasicAuth:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password