from radicale.auth import BaseAuth
from pam import pam as Pam

class Auth(BaseAuth):
    """authenticates users against PAM"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pam = Pam()

    def is_authenticated(self, username, password):
        assert username
        assert password
        return self.pam.authenticate(username, password)
