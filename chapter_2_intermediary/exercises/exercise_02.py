import os
os.system('cls')

def creat_operation(multiply):
    def execute_operation(number):
        return multiply * number
    return execute_operation

multiply_by_two = creat_operation(2)
multiply_by_three = creat_operation(3)
multiply_by_four = creat_operation(4)

print(multiply_by_two(2))
print(multiply_by_three(2))
print(multiply_by_four(2))