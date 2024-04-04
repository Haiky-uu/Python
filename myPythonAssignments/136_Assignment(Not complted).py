# Get two dates and generate a calendar dimension with following fields:
# 1. day, month, year, weekday, day of week, day of month, day of year, weekendFlag,
# 1stwkFlag,2ndwkFlag etc,3rdWkFlag,4thWkFlag,5thWkFlag,day_of_quarter

from conf2 import start_date, end_date, oneDay

cal = {}

while start_date < end_date:

    year = start_date.year
    month = start_date.month
    day = start_date.day
    weekday = start_date.isoweekday()

    if year in cal:
        if month in cal[year]:
            if day in cal[year][month]:
                cal[year][month][day].append(weekday)
            else:
                cal[year][month][day] = [weekday]
        else:
            cal[year][month] = {day: [weekday]}
    else:
        cal[year] = {month: {day: [weekday]}}

    start_date += oneDay

# print(cal)


for year, months in cal.items():
    print("Year:", year)
    for month, days_dict in months.items():
        print('Month:', month)
        for day, weekday_list in days_dict.items():
            weekday_str = ', '.join(map(str, weekday_list)) # For removing sqlre brackets
            print('Day:', day, 'Weekdays:', weekday_str)


