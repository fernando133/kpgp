import gnupg
import os
class StringHelper:
    def __init__(self, directory=None):
        self.directory = directory+'/gpghome'
