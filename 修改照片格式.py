import os
import re
import shutil

path = r"C:\Users\guanlibu\Desktop\在校生学籍照片"
file_walk = os.walk(path)
#fileNum = 0
filesPathList = []
for root,dirs,files in file_walk:
    #print(root)
    #print(dirs)
    #print(files)
    for file in files:
        #fileNum = fileNum+1
        filePath = root + '/' + file
        #print(filePath)
        filesPathList.append(filePath)
        protion = os.path.splitext(filePath)
        #print(protion[0])
        #print(protion[1])
        if protion[1].lower() == '.png':
            print("正在处理："+filePath)
            newFilePath = protion[0] + '.jpg'
            shutil.move(filePath,newFilePath)
