# -*- coding: utf-8 -*-

from PIL import Image

fp = open("test_image_8.jpg", "rb")
im = Image.open(fp)

print(im.format, "%dx%d" % im.size, im.mode)

#------------------------------------------------------------------------------
from PIL.ExifTags import TAGS, GPSTAGS
#from PIL.ExifTags import GPSTAGS

#print(PIL.VERSION, PIL.PILLOW_VERSION)
exifd = im._getexif()
print(exifd[36867])

keys = list(exifd.keys())
TAGSr = dict(((v, k) for k, v in TAGS.items())) # TAGSr czyli TAGS odwrotnie, nazwa:liczba

fp.close()
#%%
for ek, ev in exifd.items():
    print(ek,TAGS.get(ek,ek),ev)
#%%
for k, v in GPSTAGS.items():
    print(k,v) 
    #print(k if k==51041 else "",end='')
#%%
import os, hashlib
pth = r'\\KABATY\Users\Public\Pictures\card_dcim_camera'
ld = os.listdir(pth)
lj = [ld[i] for i in range(len(ld)) if     ld[i].endswith('.jpg')] # lista jpeg-ów
lm = [ld[i] for i in range(len(ld)) if not ld[i].endswith('.jpg')] # ~lista mpeg=ów 
print(len(ld),len(lj),len(lm))

def hshmd5(inpfile):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(inpfile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def allfiles(inppath):
    filelist = list()
    for root, dirs, files in os.walk(inppath):
        for file in files:
            filelist.append(os.path.join(root,file))
    return filelist

i = 1; ibreak=1
for filnm in lj:
    inpfile = pth+'\\'+filnm
    inpfsiz = os.stat(inpfile).st_size
    print(str(i).rjust(3), filnm.ljust(20), hshmd5(inpfile), inpfsiz)
    i+=1
    if i>ibreak:
        break

al1 = allfiles(pth) # wszystkie pliki w ścieżce pth (1)
    #%%
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
filnam = lj[0]
filnam = pth+"\\"+filnam
with Image.open(filnam) as im:
    print('{} {}x{}'.format(im.format, im.size[0], im.size[1]))
    exifd = im._getexif()
    im.close()