# Introduction to data types

print('Gabriel Mango')
print("Gabriel \"Mango\"")
print(r"Gabriel \"Mango\"")
print('Gabriel "Mango"')


print(11)
print(type(11))
print(-1.5)
print(type(-1.5))
print(10 == 10)
print(type(10 == 10))
print(10 == 11)
print(type(10 == 11))
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
print(bool(' '))
print(str(11) + 'b')


number = input('I will double the number you enter: ')
try:
    numero_float = float(number)
    print(f'The double of "{number}" is "{numero_float * 2}".')
except:
    print('This is not a number.')


speed = 61
car_location = 101
SPEED_RADAR = 60
LOCATION = 100
RADAR_RANGE = 1
car_passed_radar_1 = car_location >= (LOCATION - RADAR_RANGE) and car_location <= (LOCATION + RADAR_RANGE)
car_speed_at_radar_1 = speed > SPEED_RADAR
if car_speed_at_radar_1:
    print('Car speed went off the radar 1.')
if car_passed_radar_1:
    print('Car passed radar 1.')
if car_passed_radar_1 and car_speed_at_radar_1:
    print('Car was fined.')


v1 = 'a'
v2 = 'a'
v3 = 'b'
print(id(v1))
print(id(v2))
print(id(v3))


condition = True
passed_if = None
if condition:
    passed_if = True
    print('Do something')
else:
    print('Do not something.')
if passed_if is None:
    print('Did not pass the if')
if passed_if is not None:
    print('Passed thr if')
