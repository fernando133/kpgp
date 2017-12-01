import gnupg
import os
class FileHelper:
    def __init__(self, directory=None):
        self.directory = directory+'/gpghome'
