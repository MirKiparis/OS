"""Работа с форматом JSON
Создать файл формате JSON из редактора в
Создать новый объект.
Выполнить сериализацию объекта в формате JSON и записать в файл.
Прочитать файл в консоль
Удалить файл
"""
import json
import os

pat = {
    "имя": "Ира",
    "возраст": 20,
    "женат/замужем": False,
    "образование": "МИРЭА"
}
print(pat)
with open("sam.json", "w") as wf:
    json.dump(pat, wf)
with open("sam.json", "r") as rf:
    redata = json.load(rf)
print(redata)
os.remove("sam.json")
