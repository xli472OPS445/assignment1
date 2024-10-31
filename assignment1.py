#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Xin Li". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: <Xin Li>
Semester: <Fall> <2024>
Description: <This is the python script for OPS445NCC Assignment1 Version B>
'''

import sys

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    ...

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...

def after(date: str) -> str: 
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    '''
    #This is to split the data that seperated by '-' to 3 different parts: year
    month and day, and indicate the day value to be calculated +1
    '''
    year, mon, day= (int(x) for x in date.split('-'))  
    day += 1  # next day

    '''
    The lyear part is to specify whether the input year was a leap year or not,
    because there are 29 days in Feburary in a leap year.
    '''

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year

    '''
    The mon_dict is to specify the number of days in each month, and if it is a leap year and the month is 2, the number of days will be set to 29 instaed of 28'''
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
   
    '''
    if the number of days reaches to the max days of a month, the month value will add 1, and if the month calculated 12 already, it will be another year. In this case, the month and day will all set to 1 and start again the calculation.
    '''
 
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{year}-{mon:02}-{day:02}" 
# This return value is to print the final date value, and set the month and
# day to return 2 digits.


def before(date: str) -> str:
    year, mon, day= (int(x) for x in date.split('-'))  
    day -= 1  # the day before

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_flag:
        mon_dict[2] = 29
 
    if day < 1:
        mon -= 1
        if mon < 1:
            year -= 1
            mon = 12
        day = mon_dict[mon]  
    return f"{year}-{mon:02}-{day:02}" 


def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...

def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    ...

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    ...
