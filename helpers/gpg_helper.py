#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gnupg

class GpgHelper:
    
    def __init__(self, directory=None):
        self.directory = directory

    def generate_key(self, directory=None, email, passphrase):
        """
        """
        gpg = None
        if not directory is None:
            gpg = gnupg.GPG(gnupghome=directory)

        input_data = gpg.gen_key_input(name_email=email, passphrase=passphrase)
        key = gpg.gen_key(input_data)
        return key

    def export_keys(self, key):
        """
        """
        gpg = gnupg.GPG()
        if not self.directory is None:
            gpg = gnupg.GPG(gnupghome=self.directory)

        ascii_armored_public_keys = gpg.export_keys(str(key))
        ascii_armored_private_keys = gpg.export_keys(str(key), True)
        with open('kpgp-keyfile.asc', 'w') as f:
            f.write(ascii_armored_public_keys)
            f.write(ascii_armored_private_keys)
        f.close()

        #TODO comand to cat kpgp-mykeyfile.asc 

