import os, zipfile, shutil

if 'z.zip' in os.listdir():
    os.remove('z.zip')
if 'document.xml' in os.listdir('.\\sample\\word'):
    os.remove('.\\sample\\word\\document.xml')

shutil.copy('1_test_test.xml', '.\\sample\\word\\document.xml')

if 'z.docx' in os.listdir():
    os.remove('z.docx')
shutil.make_archive('z', 'zip', '.\\sample')

thisFile = "z.zip"
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".docx")