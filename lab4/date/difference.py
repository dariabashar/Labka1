from datetime import datetime

def difference(datetime_first, datetime_second):
    time = datetime_second - datetime_first
    return time.total_seconds()

def main():
    year1= int(input('Enter a year for date1: '))
    month1 = int(input('Enter a month for date1: '))
    day1 = int(input('Enter a day for date1: '))
    hours1 = int(input('Enter hours for date1: '))
    minutes1 = int(input('Enter minutes for date1: '))
    seconds1 = int(input('Enter seconds for date1: '))
    microseconds1 = int(input('Enter microseconds for date1: '))

    datetime1 = datetime(year1, month1, day1, hours1, minutes1, seconds1, microseconds1)

    year2= int(input('Enter a year for date2: '))
    month2 = int(input('Enter a month for date2: '))
    day2 = int(input('Enter a day for date2: '))
    hours2 = int(input('Enter hours for date2: '))
    minutes2 = int(input('Enter minutes for date2: '))
    seconds2 = int(input('Enter seconds for date2: '))
    microseconds2 = int(input('Enter microseconds for date2: '))

    datetime2 = datetime(year2, month2, day2, hours2, minutes2, seconds2, microseconds2)
    
    result = difference(datetime1,datetime2)
    
    print(result)
    
if __name__ == "__main__":
    main()