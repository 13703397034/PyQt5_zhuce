import os
import shutil
path = r'C:\Users\guanlibu\Desktop\学籍照片'
new_path = r'C:\Users\guanlibu\Desktop\2019学籍'

for root, dirs, files in os.walk(path):
    for i in range(len(files)):
        if (files[i][-3:] == 'jpg'or files[i][-4:] == 'jpeg'or files[i][-3:] == 'png'):
            file_path = root + '/' + files[i]
            new_file_path = new_path + '/' + files[i]
            shutil.copy(file_path, new_file_path)
