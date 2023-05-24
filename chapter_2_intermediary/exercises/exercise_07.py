import os
os.system('cls')

def is_task(message):
    if not tasks:
        print()
        print('No task for', message)
        print()

def list_task():
    print()
    if is_task('list'):
        return
    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')

def undo_task():
    print()
    if is_task('undo'):
        return
    item = tasks.pop()
    print(f'{item} has been removed from the to-do list.')
    redo_tasks.append(item)
    print()

def redo_task():
    print()
    if is_task('redo'):
        return
    item = redo_tasks.pop()
    print(f'{item} has been added to the to-do list.')
    tasks.append(item)
    print()

def add_task(task):
    print()
    task = task.strip()
    if not task:
        print('You have not entered a task.')
        return
    print(f'{task} has been added to the to-do list.')
    tasks.append(task)



tasks = []
redo_tasks = []

while True:
    print('To-do List')
    print('Commands: list, undo and redo')
    task = input('Enter a task or command: ')

    if task == 'list':
        list_task()
        continue
    elif task == 'undo':
        undo_task()
    elif task == 'redo':
        redo_task()
        continue
    elif task == 'clear':
        os.system('cls')
        continue
    else:
        add_task(task)
        list_task()
        continue
