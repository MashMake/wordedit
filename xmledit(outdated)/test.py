import os, shutil, random
from docx import Document
# s = [random.randint(1, 100) for i in range(9)]
# print(s)

# # thisFile = "z.zip"
# # base = os.path.splitext(thisFile)[0]
# # os.rename(thisFile, base + ".docx")

# # shutil.make_archive('x', 'zip', '.\\sample')
# if '1_test.txt' in os.listdir():
#     os.remove('1_test.txt')
# shutil.copy('1_test.xml', '1_test.txt')

# with open('1_test.txt', 'r') as file:
#     filedata = file.read()

# for i in range(9):
#     print(str(i+1) + '*', str(s[i]))
#     filedata.replace(str(i) + '*', str(s[i]))

# with open('1_test.txt', 'w') as file:
#   file.write(filedata)

# # os.remove('1_test.xml')
# # shutil.copy('1_test.txt', '1_test.xml')

doc = Document('0.docx')
table = doc.tables[0]
print(table.style)