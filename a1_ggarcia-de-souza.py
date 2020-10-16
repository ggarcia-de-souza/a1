#!/usr/bin/env python3
''' This script will take a date of birth in different formats-"YYYYMMDD", "YYYY/MM/DD", "YYYY-MM-DD"-and it will turn it
into a standard format "mmm d, yyyy"
For example, if the user enters  "20201007", or "2020-10-07", or "2020/10/07", or "2020.10.07", the script will return "Oct 7, 2020". 
-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_ggarcia-de-souza.py (replace [Seneca_name] with your Seneca User name)
Author: Guilherme Garcia de Souza
The python code in this file (a1_ggarcia-de-souza.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(year):
    '''
    This function will take a year and return True if it is a Leap Year. False is it is not a Leap Year
    '''

    
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return  True  
            else:  
                return False  
        else:  
            return True
    else:  
        return False 

  

def sanitize(obj1):
    '''
    This function will take a date, and it will remove special characters like "-","/","."
    It will return the date with spaces between the year, month and day
    '''
    
    if "/" in obj1:
        obj2 = obj1.replace('/',' ')
        
    elif "-" in obj1:
        obj2 = obj1.replace('-',' ')

    elif "." in obj1:
        obj2 = obj1.replace('.',' ')
      
    else:
        obj2 = obj1[0:4] + ' ' + obj1[4:6]  + ' ' + obj1[6:]
  
    return obj2   
    

def size_check(obj):
    '''
    This function will check the size of the argument. If the size is equal to 10, it will return True. If not, it will return False
    '''
    if len(obj) == 10:
        return True
    else:
        return False

def range_check(obj1, obj2):
    '''
    This function will take two objects-one is an integer and the seoond is a tuple. It will return True if the the first object is between the first element    and the second element of the tuple.
    '''
    if obj1 >= obj2[0] and obj1 <= obj2[1]:
        return True
    else:
        return False
    
def usage():    
    '''
    This fnction will return the usage of this script.
    '''
    return "Usage: a1_ggarcia-de-souza.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"

    
if __name__ == "__main__":
    '''
    I need to finish this part!

    '''

    if len(sys.argv) != 2:
        print(usage())
        sys.exit()
    
    user_input = sanitize(sys.argv[1])
    
    if size_check(user_input) is False:
               
        print("Error 09: wrong date entered")
        sys.exit()
   

    print(result)  
    


