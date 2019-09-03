# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:12:25 2019

@author: Student
"""
import string
def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict = {}
        #dictlower = {}
        dictupper = {}
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        shiftlower = lower[shift:]+lower[0:shift]
        shiftupper = upper[shift:]+upper[0:shift]
        #print('lower=',lower)
        #print('shift=',shiftlower)
        for i in range(len(lower)):
            dict.__setitem__(lower[i],shiftlower[i])

        j = 0
        while j < len(upper):
         
             dictupper.__setitem__(upper[j],shiftupper[j])
             j+=1

        dict.update(dictupper)
        #print(dict)

 def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        CaesarS = ''
        dict = build_shift_dict(self,shift)
        for c in self.message_text:
            if c in dict:
                CaesarS += dict[c]
        return CaesarS        
a = apply_shift(2)