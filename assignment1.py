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

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False 

def mon_max(month:int, year:int) -> int:

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str: 

    year, mon, day= (int(x) for x in date.split('-'))  
    day += 1  # next day

    mon_max_days = mon_max(mon, year)

    if day > mon_max_days:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{year}-{mon:02}-{day:02}" 


def before(date: str) -> str:
    year, mon, day= (int(x) for x in date.split('-'))  
    day -= 1  # the day before
 
    if day < 1:
        mon -= 1
        if mon < 1:
            year -= 1
            mon = 12
        day = mon_max(mon, year)  
    return f"{year}-{mon:02}-{day:02}" 


def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...

def dbda(start_date: str, step: int) -> str:
    year, mon, day= (int(x) for x in start_date.split('-'))  

    if step > 0:    
        x = 0
        while x < step:
            start_date = after(start_date)
            x += 1
        return start_date
 
    if step < 0:    
        x = 0
        while x > step:
            start_date = before(start_date)
            x -= 1
        return start_date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    ...
