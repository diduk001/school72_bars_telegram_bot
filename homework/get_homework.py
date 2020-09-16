# Получение домашки в виде JSON через API

import requests     # Нужен, чтобы совершать HTTP-запросы
from json import loads, dumps   # Нужен, чтобы переводить JSON в структуры данных Python и обратно

# url для обращения к API получения домашки
url = 'https://school.72to.ru/api/HomeworkService/GetHomeworkFromRange'

# Заголовки-куки, необходимые, чтобы зайти на аккаунт 
header = {
    'Cookie': 'TABUN_BS=%5B%220e2880c25363b59cc84f9ef723bf6f07%22%2C%22e98c32aa1a4d607053adb884b3ca5f8c%22%5D; sessionid=r45g1btntuimvx0yrb484abocoliacwg'
}

# Получение ответа на GET запрос с куки
homeworks_resp = requests.get(url, headers=header)

# Запись JSON-ответа в файл homeworks.json
with open('homeworks.json', mode='w') as wfile:
    wfile.write(dumps(loads(homeworks_resp.content.decode()), indent=2))
