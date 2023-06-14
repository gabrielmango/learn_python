from datetime import datetime
import os

os.system('cls')

date_1 = datetime(2020, 3, 16)
print(date_1)

date_2 = datetime(2020, 3, 16, 15, 30)
print(date_2)

date_str_date = '2022-5-31 19:00:00'
data_str_fmt = '%Y-%m-%d %H:%M:%S'
date_3 = datetime.strptime(date_str_date, data_str_fmt)
print(date_3)

date_4 = datetime.now()
print(date_4)

date_5 = date_4.timestamp()
print(date_5)

date_6 = datetime.fromtimestamp(1476680222)
print(date_6)

os.system('cls')

fmt = '%d/%m/%Y %H:%M:%S'
start_date = datetime.strptime('20/04/1987 09:30:30', fmt)
end_date = datetime.strptime('12/12/2022 08:20:20', fmt)

print(f'{start_date} == {end_date}: {start_date == end_date}')
print(f'{start_date} > {end_date}: {start_date > end_date}')
print(f'{start_date} < {end_date}: {start_date < end_date}')
print()

delta = end_date - start_date
print(delta)
print(delta.total_seconds())
print(delta.days, delta.seconds, delta.microseconds)

os.system('cls')

date_7 = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(date_7.strftime('%d/%m/%Y'))
print(date_7.strftime('%d/%m/%Y %H:%M'))
print(date_7.strftime('%d/%m/%Y %H:%M:%S'))