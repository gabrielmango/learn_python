# CPF validator

import os
os.system('cls')


while True:

    cpf = input('Enter your cpf:  ')

    try:
        test_cpf = int(cpf)
        os.system('cls')
    except:
        print('Enter only numbers!')
        continue

    if len(cpf) < 11:
        print('CPF number must have eleven digits!')
        continue

    is_sequence = cpf == cpf[0] * len(cpf)
    if is_sequence:
        print('Do not enter sequences!')
        continue

    if '.' in cpf or '-' in cpf:
        cpf_without_mask = cpf.replace('.', '').replace('-', '').replace(' ', '')    
    else:
        cpf_without_mask = cpf


    nine_digits = cpf_without_mask[:9]
    regressive_counter = len(nine_digits) + 1
    result = 0
    for digit in nine_digits:
        result += int(digit) * regressive_counter
        regressive_counter -= 1
    first_digit_cpf = (result * 10) % 11
    first_digit_cpf = 0 if first_digit_cpf > 9 else first_digit_cpf
    # print(first_digit_cpf)


    ten_digits = cpf_without_mask[:9] + str(first_digit_cpf)
    regressive_counter = len(ten_digits) + 1
    result = 0
    for digit in ten_digits:
        result += int(digit) * regressive_counter
        regressive_counter -= 1
    segund_digit_cpf = (result * 10) % 11
    segund_digit_cpf = 0 if segund_digit_cpf > 9 else segund_digit_cpf
    # print(segund_digit_cpf)

    cpf_generated = ten_digits + str(segund_digit_cpf)

    if cpf_without_mask == cpf_generated:
        print('valid CPF!')
    else: 
        print('invalid CPF')
