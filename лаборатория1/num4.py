"""Работа с форматом XML
Создать файл формате XML из редактора
Записать в файл новые данные из консоли .
Прочитать файл в консоль.
Удалить файл.
"""
import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")

