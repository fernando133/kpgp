#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gnupg
import os
class GpgHelper:
    
    def __init__(self, directory=None):
        self.directory = directory
        os.system('rm -rf '+self.directory+'/gpghome')

    def generate_key(self, email, passphrase):
        """
        Generate a new key
        """
        gpg = None
        if not self.directory is None:
            gpg = gnupg.GPG(gnupghome=self.directory+'/gpghome')

        input_data = gpg.gen_key_input(name_email=email, passphrase=passphrase)
        key = gpg.gen_key(input_data)
        return key

    def export_keys(self, key):
        """
        Export the keys to a file
        """
        gpg = gnupg.GPG()
        if not self.directory is None:
            gpg = gnupg.GPG(gnupghome=self.directory+'/gpghome')

        ascii_armored_public_keys = gpg.export_keys(str(key))
        ascii_armored_private_keys = gpg.export_keys(str(key), True)
        with open('kpgp-keyfile.asc', 'w') as f:
            f.write(ascii_armored_public_keys)
            f.write(ascii_armored_private_keys)
        f.close()
        os.system('cat kpgp-keyfile.asc')
