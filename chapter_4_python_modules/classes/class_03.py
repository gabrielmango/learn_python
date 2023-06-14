import os
import calendar
import locale

os.system('cls')

print(calendar.month(2022, 12))

locale.setlocale(locale.LC_ALL, '')

print(calendar.month(2022, 12))