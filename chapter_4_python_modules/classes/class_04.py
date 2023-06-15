import os
import shutil 

os.system('cls')

PATH = os.path.join('desktop', 'file.txt')
print(PATH)

directory, file = os.path.split(PATH)
print(directory)
print(file)

print(os.path.exists(PATH))

CLASS_04_PATH = os.path.abspath('class_04.py')
print(CLASS_04_PATH)

print(os.path.basename(CLASS_04_PATH))

print(os.path.dirname(CLASS_04_PATH))

os.system('cls')

PATH_CHAPTER_1 = os.path.abspath('chapter_1_introdution')
print(PATH_CHAPTER_1)

print(os.listdir(PATH_CHAPTER_1))

for folder in os.listdir(PATH_CHAPTER_1):
    FULL_PATH = os.path.join(PATH_CHAPTER_1, folder)
    
    if not os.path.isdir(FULL_PATH):
        continue

    for item in os.listdir(FULL_PATH):
        print(item)

os.system('cls')
    
PATH_CHAPTER_2 = os.path.abspath('chapter_2_intermediary')

for root, dirs, files in os.walk(PATH_CHAPTER_2):

    for file in files:
        FULL_PATH_CAPTER_2 = os.path.join(root, file)
        print(FULL_PATH_CAPTER_2)
        
os.system('cls')

PATH_CHAPTER_3 = os.path.abspath('chapter_3_object_oriented')

PATH_DIR = os.path.dirname(PATH_CHAPTER_3)

BACKUP_FOLDER = os.path.join(PATH_DIR, 'backup_chapter_3')

os.makedirs(BACKUP_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(PATH_CHAPTER_3):
    for dir in dirs:
        NEW_PATH_DIR_BACKUP = os.path.join(
            root.replace(PATH_CHAPTER_3, BACKUP_FOLDER), dir
        )
        os.makedirs(NEW_PATH_DIR_BACKUP, exist_ok=True)

    for file in files:
        NEW_PATH_FILE = os.path.join(root, file)
        NEW_PATH_FILE_BACKUP = os.path.join(
            root.replace(PATH_CHAPTER_3, BACKUP_FOLDER), file
        )
        shutil.copy(NEW_PATH_FILE, NEW_PATH_FILE_BACKUP)


