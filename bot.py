import vk_api
import math
import random
from settings import *
from data import *
from ejudge import *
from vk_api.longpoll import VkLongPoll, VkEventType
import json

def write_msg(user_id, message):
	vk.method('messages.send', {'user_id' : user_id, 'message' : message, 'random_id': random.randint(1, 10**12), "keyboard" : keyboard})

def write_img(user_id, attachment):
	vk.method('messages.send', {'user_id' : user_id, 'attachment' : attachment, 'random_id': random.randint(1, 10**12), "keyboard" : keyboard})

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [

    [get_button(label="расписание звонков", color="positive"),
    get_button(label="расписание", color="primary")],
    [get_button(label="ejudge", color="primary")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			request = event.text
			if "расписание звонков" in request:
				write_msg(event.user_id, rings)
			elif "расписание" in request:
				if "понедельник" in request:
					write_img(event.user_id, 'photo-175382124_456239020')
				elif "вторник" in request:
					write_img(event.user_id, 'photo-175382124_456239024')
				elif "среда" in request:
					write_img(event.user_id, 'photo-175382124_456239023')
				elif "четверг" in request:
					write_img(event.user_id, 'photo-175382124_456239022')
				elif "пятница" in request:
					write_img(event.user_id, 'photo-175382124_456239019')
				else:
					write_img(event.user_id, 'photo-175382124_456239021')
			elif "чистка" in request:
				write_msg(event.user_id, isClear(http://ejudge.cfuv.ru/2018/III_semestr/standings/standings048.html))
			elif "ejudge" in request:
				write_msg(event.user_id, get_ans(http://ejudge.cfuv.ru/2018/III_semestr/standings/standings048.html))
			else:
				write_msg(event.user_id, ".")



