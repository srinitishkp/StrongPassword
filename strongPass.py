#!/bin/python3

import math
import os
import random
import re
import sys
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    sp_list=[0,0,0,0]
    length=False
    if(n>6):
        length=True
    for i in password:
        if(i in numbers):
            sp_list[0]+=1
        elif(i in lower_case):
            sp_list[1]+=1
        elif(i in upper_case):
            sp_list[2]+=1
        elif(i in special_characters):
            sp_list[3]+=1
    if(length):
        return sp_list.count(0)                    
    else:
        return max(sp_list.count(0),(6-n))    
if __name__ == '__main__':
    

    n = int(input("Enter the length of the password"))

    password = input("Enter the password")

    answer = minimumNumber(n, password)

    print("Minimum no. of characters to make a strong password",answer)

    

