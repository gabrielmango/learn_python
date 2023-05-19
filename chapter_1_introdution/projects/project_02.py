# Generator CPF

import random
import os

os.system('cls')

ninge_digits_generated = ''
for i in range(9):
    ninge_digits_generated += str(random.randint(0, 9))

regressive_counter = len(ninge_digits_generated) + 1
result = 0
for digit in ninge_digits_generated:
    result += int(digit) * regressive_counter
    regressive_counter -= 1
first_digit_cpf = (result * 10) % 11
first_digit_cpf = 0 if first_digit_cpf > 9 else first_digit_cpf


ten_digits = ninge_digits_generated + str(first_digit_cpf)
regressive_counter = len(ten_digits) + 1
result = 0
for digit in ten_digits:
    result += int(digit) * regressive_counter
    regressive_counter -= 1
segund_digit_cpf = (result * 10) % 11
segund_digit_cpf = 0 if segund_digit_cpf > 9 else segund_digit_cpf

cpf_generated = ten_digits + str(segund_digit_cpf)

print(cpf_generated)

