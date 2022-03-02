"""Работа с форматом XML
Создать файл формате XML из редактора
Записать в файл новые данные из консоли .
Прочитать файл в консоль.
Удалить файл.
"""
import xml.etree.cElementTree as ET
import os
root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")

tree = ET.parse('filename.xml')
root = tree.getroot()
doc = root[0]
for child_of_root in doc:
    # print(child_of_root.tag, child_of_root.attrib)
    print(child_of_root.tag, '>> измените текст >> ')
    child_of_root.text = input()

tree.write("filename.xml")
f = open('filename.xml', 'r')
print(f.read())
f.close()
os.remove("filename.xml")
