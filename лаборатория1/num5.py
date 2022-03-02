"""5.   Создание zip архива, добавление туда файла, определение размера архива
•  Создать архив в форматер zip
•  Добавить файл в архив
•  Разархивировать файл и вывести данные о нем
•  Удалить файл и архив
"""
import zipfile
import os


s = "second.txt"
f = open(s, 'w')
f.write("What's the HELL!!!!aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
f.close()

print('Creating Archive.zip.')
archive = zipfile.ZipFile('Archive.zip', mode='w', compression = zipfile.ZIP_DEFLATED)
try:
    archive.write(s, arcname=s)
finally:
    archive.close()
    os.remove(s)
    print('Extracting ZIP.')
    archive = zipfile.ZipFile('Archive.zip','r', compression = zipfile.ZIP_DEFLATED)
    archive.extractall('.')
    print('ZIP Extracted.')
    for file_info in archive.infolist():
        print(file_info.filename, " >>> " , file_info.date_time," >>> " , file_info.file_size , " >>>> ", file_info.compress_size)
        os.remove(file_info.filename)
    archive.close()
    os.remove('Archive.zip')
