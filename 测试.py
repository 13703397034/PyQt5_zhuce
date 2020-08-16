from PIL import Image, ExifTags
#img = Image.open(r'C:\Users\guanlibu\Desktop\在校生更正照片\17L1104133.jpg')
img = Image.open(r"IMG_20191210_073931_BURST009.jpg")

for orientation in ExifTags.TAGS.keys() :
    if ExifTags.TAGS[orientation]=='Orientation' : break
exif=dict(img._getexif().items())
if   exif[orientation] == 3 :
    img=img.rotate(180, expand = True)
    img =img.save()
elif exif[orientation] == 6 :
    img=img.rotate(270, expand = True)
elif exif[orientation] == 8 :
    img=img.rotate(90, expand = True)
print('OK')
