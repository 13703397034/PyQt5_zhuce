from PIL import Image
import os
import shutil
path = r'C:\Users\guanlibu\Desktop\在校生学籍照片'
news = r'C:\Users\guanlibu\Desktop\在校生更正照片'
for root, dirs, files in os.walk(path):
    for file in files:
        filePath = root +'/'+ file
        protion = os.path.splitext(filePath)
        if protion[1].lower() == '.png'or protion[1] == '.jpeg'or protion[1]=='.JPG':
            print("正在处理："+filePath)
            newFilePath = protion[0] + '.jpg'
            shutil.move(filePath,newFilePath)
    '''for i in range(len(files)):
        im = Image.open(path+'/'+files[i])
        if im.size[0]>im.size[1]:
            out = im.transpose(Image.ROTATE_270)
            out.save(news+'\\'+files[i])
            print(out.size[0],out.size[1])
            '''