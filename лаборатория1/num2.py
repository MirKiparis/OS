"""Работа с файлами ( класс File, FileInfo, FileStream и другие)
Создать файл
Записать в файл строку
Прочитать файл в консоль
Удалить файл
"""
import os
f = open("text.txt", 'w')
s = input("Введите строку: \n")
f.write(s + '\n')
f.close()
f = open("text.txt")
print(f.read())
f.close()
os.remove("text.txt")
