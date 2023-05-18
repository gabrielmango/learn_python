import os
os.system('cls')

to_do_list = []

while True:
    print('Select an option:')
    option = input('[i]nsert [d]elet [l]ist:  ')

    if option == 'i':
        os.system('cls')
        value = input('Value: ')
        to_do_list.append(value)
    elif option == 'd':
        informed_index = input('Choose the index to delete:')
        try:
            index = int(informed_index)
            del to_do_list[index]
        except:
            print('Unable to delete this index.')
    elif option == 'l':
        os.system('cls')
        if len(to_do_list) == 0:
            print('Nothing to list.')
        else:
            for i, value in enumerate(to_do_list):
                print(i, value)
    else:
        print('Invalid option.')

