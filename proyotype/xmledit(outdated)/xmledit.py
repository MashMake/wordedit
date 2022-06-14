import xml.etree.ElementTree as ET
import random

s = [random.randint(0, 100) for i in range(9) ]
print(s)

tree = ET.parse('1_test.xml')
root = tree.getroot()

print(root[0][3][2][0][1][1][1].tag)

f = []

for i in range(3):
    for j in range(3):
        root[0][3][i + 2][j][1][1][1].text = s[i * 3 + j]
        f.append(root[0][3][i + 2][j][1][1][1].text)

for i in range(3):
    for j in range(3):
        print(root[0][3][i + 2][j][1][1][1].text)


tree.write('output.txt')