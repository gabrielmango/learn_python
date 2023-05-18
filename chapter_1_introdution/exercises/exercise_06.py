import os
os.system('cls')

secret_word = 'ocean'
correct_letters = ''
number_attempts = 0

while True:
    
    typed_letter = input('Enter a letter: ')

    if len(typed_letter) > 1:
        print('Enter just one letter.')
        continue
    
    if typed_letter in secret_word:
        correct_letters += typed_letter

    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'
    print(f'The secret word is: {formed_word}')

    if formed_word == secret_word:
        os.system('cls')
        print(f'You won! The secret word was "{secret_word}"')
        print(f'You hit it with {number_attempts} attempts')
        break
    else:
        number_attempts += 1

