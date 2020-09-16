# Парсим schedule.json, чтобы добыть расписание

import json # Чтобы работать с json-данными
import pprint


with open("schedule.json") as rfile:
    d = json.loads(rfile.read())

# d - словарь, в котором есть только d["days"]
# d["days"] - список расписания на дни недели
# d["days"][i] - расписание на i-й день недели
# Если в d["days"][i] нет lessons - уроков нет
# Если в d["days"][i]["is_weekend"] == True - выходной
# d["days"][i]["lessons"] - список уроков на i-й день недели 
# d["days"][i]["lessons"][j] - словарь урока на i-й день недели, j-й урока
# lesson = d["days"][i]["lessons"][j]
# lesson["discipline"] - урок
# lesson["office"] - кабинет
# lesson["teacher"] - учитель
# lesson["time_begin"] - время начала в формате ЧЧ:ММ:СС
# lesson["time_end"] - время конца в формате ЧЧ:ММ:СС

date = "2020-09-15"

days = d["days"]

for day in days:
    if day["date"] == date:
        if "lessons" not in day.keys():
            print("Нет уроков")
            break
        
        for lesson in day["lessons"]:
            discipline = lesson["discipline"]
            office = lesson["office"]
            teacher = lesson["teacher"]
            time_begin = lesson["time_begin"]
            time_end = lesson["time_end"]

            print(discipline, office, teacher, time_begin, time_end, sep='\n', end='\n' + '-'*10 + '\n')