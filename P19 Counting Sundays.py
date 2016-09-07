'''
P19 Counting Sundays
    You are given the following information, but you may prefer to do some 
    research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a 
        century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century 
    (1 Jan 1901 to 31 Dec 2000)?
'''

def answer():
    num_sundays = 0
    sunday = 6
    feb_month = 1
    shorter_months = [3, 5, 8, 10]# Shift down by one 
    
    starting_day = start_from_1900() # The week day of 1 Jan 1901
    if starting_day == sunday:
        num_sundays += 1
    for year in range(1901, 2001):
        for month in range(12):
            if month == feb_month:
                if is_leap(year):
                    starting_day = (starting_day + 29) % 7
                else:
                    starting_day = (starting_day + 28) % 7
            elif month in shorter_months:
                starting_day = (starting_day + 30) % 7
            else:
                starting_day = (starting_day + 31) % 7
            if starting_day == sunday:
                num_sundays += 1
    return num_sundays
        
def start_from_1900():
    # Start with Monday 1 Jan 1900. Return the weekday of 1 Jan 1901
    year = 1900
    if is_leap(year):
        year_len = 366
    else:
        year_len = 365
    return year_len % 7

def is_leap(year):
    if year % 100 == 0: # If year is a century
        if year % 400 == 0: 
            return True
    elif year % 4 == 0:
        return True
    return False

if __name__ == "__main__":
    print answer() # 171