#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:11:09 2020

@author: home
"""

#basic hello world example from book

print('Hello World')
print ("Gimme your name:")

theirName = input()

print ("Welcome "+theirName+"!")
print ("Your value is determined by your name. It is:")
print(len(theirName))
print("\nHow old are you, "+theirName+"?")
theirAge = input()

print ("\nNext year, you will be "+ str(int(theirAge) +1)+". You old.")

#well, at least I know print statements again 