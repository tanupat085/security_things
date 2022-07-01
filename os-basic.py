import os
import random
import time
import shutil

path = r'D:\CODE\sec'

folder = os.listdir(path)

result_file = []
result_folder = []
file_dict = {}

#print(folder)
for fd in folder:
    check = fd.split('.')
    if len(check) > 1:
        #print('File: ',fd)
        result_file.append(fd)
    else:
        #print('Fiolder: ',fd)
        result_folder.append(fd)

# print('fd: ',result_folder)
# print('fl: ',result_file)

for f in result_file:
    select = random.choice(result_folder)
    folderpath = os.path.join(path,select)
    filepath = os.path.join(folderpath,f)
    current = os.path.join(path,f)
    # print(current,'----->',filepath)
    file_dict[f] = {'current':current , 'next':filepath}

print(file_dict)

for fk,fv in file_dict.items():
    current = fv['current']
    nextpath = fv['next']
    shutil.move(current,nextpath)

    select = random.choice(result_folder)
    folderpath = os.path.join(path,select)
    file_next = os.path.join(folderpath,fk)
    file_dict[fk]['current'] = nextpath
    file_dict[fk]['next'] = file_next

    print('next: ',file_dict)