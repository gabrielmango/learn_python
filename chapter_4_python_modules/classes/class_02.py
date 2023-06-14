import calendar

import os

os.system('cls')

year_2022 = calendar.calendar(2022)
print(year_2022)

print('-' * 100)

december_2022 = calendar.month(2022, 12)
print(december_2022)

print('-' * 100)

last_day_dezember_2022 = calendar.monthrange(2022, 12)
print(last_day_dezember_2022)
print(list(enumerate(calendar.day_name)))

day_number, last_day = calendar.monthrange(2022, 12)
print(calendar.day_name[day_number])

print('-' * 100)

calendar_dezember_2022 = calendar.monthcalendar(2012, 12)
print(calendar_dezember_2022)

for week in calendar_dezember_2022:
    print(week)