from docx import Document

document = Document("1.docx")
with open("1_test.xml", 'w') as f:
    f.write(document._element.xml)

# document.add_table(3, 4)
# document.save("1_new.docx")
# with open("1_new.xml", 'w') as f:
#     f.write(document._element.xml)