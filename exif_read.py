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
#ptht = r'\\KABATY\Users\Public\Pictures\card_dcim_camera'
ptht = r'c:\Users\Public\Pictures\card_dcim_camera'
ld = os.listdir(ptht)
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

rdic = dict() # na dane o plikach (zdjęciach) z 'recordings'
tdic = dict() # na dane o plikach (zdjęciach) z 'telefonu'

pthr = r'r:\recordings'
alr = allfiles(pthr) # wszystkie pliki w ścieżce pthr (recordings)
alt = allfiles(ptht) # wszystkie pliki w ścieżce ptht (z telefonu)

i = 1; ibreak=2
for f in alr:
    filn = f.split('\\')[-1]
    fsiz = os.stat(f).st_size
    fhsh = hshmd5(f)
    rdic[f] = filn, fsiz, fhsh
    print(str(i).rjust(5), filn.ljust(30), fhsh, fsiz)
    i += 1
    if i>ibreak:
        break

i = 1; ibreak=2
for filn in lj: #   pętla po zdjęciach 'z telefonu'
    f = ptht+'\\'+filn
    fsiz = os.stat(f).st_size
    fhsh = hshmd5(f)
    tdic[f] = filn, fsiz, fhsh
    print(str(i).rjust(5), filn.ljust(30), fhsh, fsiz)
    i+=1
    if i>ibreak:
        break
#%%
rdic = dict()
tdic = dict()

    #%%
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
filnam = lj[0]
filnam = ptht+"\\"+filnam
with Image.open(filnam) as im:
    print('{} {}x{}'.format(im.format, im.size[0], im.size[1]))
    exifd = im._getexif()
    im.close()