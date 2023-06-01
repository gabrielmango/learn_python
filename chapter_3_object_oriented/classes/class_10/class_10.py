import os
from pathlib import Path
from contextlib import contextmanager

os.system('cls')

class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Opening the file.')
        self._file = open(self.file_path, self.mode, encoding = 'utf8')
        return self._file
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing the file.')
        self._file.close()

FOLDER_PATH = Path(__file__).parent
FILE_PATH = f'{FOLDER_PATH}\class_10a.txt'


with MyOpen(FILE_PATH, 'a') as file:
    file.write('Testing...\n')

os.system('cls')

def my_open(file_path, mode):
    try:
        print('Opening the file.') 
        file_ = open(file_path, mode, encoding = 'utf8')
        yield file_
    except Exception as error:
        print('Error occurred', error)
    finally:
        print('Closing the file.')
        file_.close()

FILE_PATH_2 = f'{FOLDER_PATH}\class_10b.txt'
with my_open(FILE_PATH_2, 'a') as file:
    file.write('Testing...\n')