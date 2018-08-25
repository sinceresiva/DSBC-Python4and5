# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 14:31:34 2018

@author: Siva
"""
import numpy as np
from random import randint

class Cipher:
    key = randint(1, 50)
    
    def __init__(self, textToEncode):
        self.stringToEncode=textToEncode   
        self.encString=""
        self.decString=""
        print("Encrypting {} with {}".format(self.stringToEncode, Cipher.key))

    def encrypt(self):
        for chrr in list(self.stringToEncode):  
            if(chrr.isalpha() or chrr.isnumeric()):
                self.encString+=chr(ord(chrr)+Cipher.key)
       
    def decrypt(self):
        for chrr in list(self.encString):    
            self.decString+=chr(ord(chrr)-Cipher.key)
        
text=input("Enter string to encrypt:")
cipherObject = Cipher(text)
cipherObject.encrypt()
print("Encrypted String: {}".format(cipherObject.encString))
cipherObject.decrypt()
print("Decrypted String: {}".format(cipherObject.decString))