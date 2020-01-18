"""
Calculates the number of sundays happening in the first of the month from january 1st 1901 to december 31st 2000
Author: Juan Rios
"""
import math

"""
Number of sunday in the 20th century
"""
def total_sundays():
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    current_day = days_in_month[0]+1 # first of the month 
    sunday_counter = 0
    for days in days_in_month[1:]:
        current_day += days
    current_year = 1901
    while (True):
        for i in range(len(days_in_month)):
            if i == 1:
                if current_year % 4 == 0:
                    if current_year%100!=0 or current_year % 400 == 0:
                        current_day += 29
                    else:
                        current_day += days_in_month[i]
                else:
                    current_day += days_in_month[i]
            else:
                current_day += days_in_month[i]
            if current_day % 7 == 0:
                sunday_counter += 1
        current_year += 1
        if current_year == 2001:
            return sunday_counter
    
if __name__ == "__main__":
    print('The number of sundays in the first of the month for the 20th century is {0}'.format(total_sundays()))
