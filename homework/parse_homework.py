# Парсим homeworks.json, чтобы добыть домашку

import json     # Нужен, чтобы переводить JSON в питоновские объекты

# Читаем файл homeworks.json, делаем из него список словарей
with open("homeworks.json") as rfile:
    d = json.loads(rfile.read())

# d[i] - i-й день недели
# d[i]['date'] - дата
# d[i]['discipline'] - урок
# d[i]['homework'] - домашка на этот урок
# d[i]['nextHomework'] - домашка на следующий урок
# d[i]['teacher'] - учитель

# Дата, за которую мы хотим получить данные
date = "2020-09-14"

# Проходимся по дням
for day in d:
    # Если дата такая , какую мы хотим
    if day['date'] == date:
        # Проходимся по домашкам
        for lesson in day['homeworks']:
            # Печатаем урок, домашку, следующую домашку, учителя
            discipline = lesson['discipline']
            homework = lesson['homework']
            next_homework = lesson['nextHomework']
            teacher = lesson['teacher']

            print(discipline, homework, next_homework, teacher, sep=' \n', end='\n' + '-' * 10 + '\n')