# Получение расписания в виде JSON через API

import requests     # Нужен, чтобы совершать HTTP-запросы
from json import loads, dumps   # Нужен, чтобы переводить JSON в структуры данных Python и обратно

# url для обращения к API получения расписания
url = 'https://school.72to.ru/api/ScheduleService/GetWeekSchedule'

# Заголовки-куки, необходимые, чтобы зайти на аккаунт 
header = {
    'Cookie': 'TABUN_BS=%5B%220e2880c25363b59cc84f9ef723bf6f07%22%2C%22e98c32aa1a4d607053adb884b3ca5f8c%22%5D; sessionid=r45g1btntuimvx0yrb484abocoliacwg'
}

# URL-параметр дата
params = {
    'date': '2020-09-15'
}

# Получение ответа на GET запрос с куки
schedule_resp = requests.get(url, headers=header, params=params)
print(schedule_resp.url)
# Запись JSON-ответа в файл schedule.json
with open('schedule.json', mode='w') as wfile:
    wfile.write(dumps(loads(schedule_resp.content.decode()), indent=2))

'''
curl 'https://school.72to.ru/api/ScheduleService/GetWeekSchedule?date=2020-09-15' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://school.72to.ru/personal-area/' \
  -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Cookie: TABUN_BS=%5B%220e2880c25363b59cc84f9ef723bf6f07%22%2C%22e98c32aa1a4d607053adb884b3ca5f8c%22%5D; sessionid=r45g1btntuimvx0yrb484abocoliacwg' \
  --compressed
'''