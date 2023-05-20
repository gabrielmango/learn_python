import os
os.system('cls')

questions = [
    {
        'question': 'how much is 1 + 1?',
        'options': ['1', '2', '3', '4'],
        'answer': '2',
    },
    {
        'question': 'how much is 5 * 5?',
        'options': ['25', '50', '55', '125'],
        'answer': '25',
    },
    {
        'question': 'how much is 10 / 2?',
        'options': ['1', '2', '4', '5'],
        'answer': '5',
    },
]

points = 0

for question in questions:
    print('Question:', question['question'])
    print()

    for i, option in enumerate(question['options']):
        print(f'{i}) {option}')
    print()

    choice = input('choose an option:  ')

    if question['answer'] == choice:
        points += 1
        print('Right answer!')
    else:
        print('Incorrect answer!')

print()
print(f'You got {points} questions right!')