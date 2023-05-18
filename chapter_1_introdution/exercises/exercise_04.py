import os
os.system('cls')

hour = input('Enter the time in whole numbers:')
try:
    hour = int(hour)

    if hour >= 0 and hour < 11:
        print('good morning!')
    if hour >= 11 and hour < 18:
        print('good afternoon!')
    if hour >= 18 and hour < 0:
        print('goodnight!')        
except:
    print('I do not know this time.') 