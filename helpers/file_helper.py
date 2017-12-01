#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gnupg
import os
class FileHelper:
    def __init__(self, directory=None):
        self.directory = directory+'/gpghome'
