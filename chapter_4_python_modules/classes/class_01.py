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

