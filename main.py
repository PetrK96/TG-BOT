import requests
import time

API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "6704589031:AAFuUU94ZpKZPO6CzIHvQzCxXJJDuYBCNqI"
TEXT = "Ура, замечено обновление"
MAX_COUNTER = 100

offset = -2 #Что это??
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print('attempt = ', counter) #чтобы видеть в консоли кол-во повторений в консоле
    updates = requests.get('{}{}/getUpdates?offset={}'.format(API_URL, BOT_TOKEN, offset + 1)).json()

    if updates["result"]:
        for result in updates['result']:
            offset = result["update_id"]
            chat_id = result['message']["from"]["id"]
            name = result['message']['from']['first_name'] + " " + result['message']['from']['last_name']

            requests.get("{}{}/sendMessage?chat_id={}&text={}, {}".format(API_URL, BOT_TOKEN, chat_id, TEXT, name))

    time.sleep(1)
    counter += 1

