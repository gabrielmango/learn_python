import os
os.system('cls')

path = r'C:\\github_gabrielmango\\learn_python\\chapter_2_intermediary\\classes\\class_09.txt'

with open(path, 'w+', encoding='utf-8') as file:
    file.write('Line 1 \n')
    file.write('Line 2 \n')

    file.writelines(
        ('Line 3 \n', 'Line 4 \n')
    )

    file.seek(0,0)
    print(file.read())

# with open(file_path, 'r') as file_txt:
#     print(file_txt.read())

os.rename(path, 'test.txt')
os.remove(path)
