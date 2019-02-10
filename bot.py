import vk_api
import math
import random
from settings import *
from data import *
from ejudge import *
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id' : user_id, 'message' : message, 'random_id': random.randint(1, 10**12)})

def write_img(user_id, attachment):
    vk.method('messages.send', {'user_id' : user_id, 'attachment' : attachment, 'random_id': random.randint(1, 10**12)})

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
        			write_img(event.user_id, 'photo294605837_456246513')
        		elif "вторник" in request:
        			write_img(event.user_id, 'photo294605837_456246515')
        		elif "среда" in request:
        			write_img(event.user_id, 'photo294605837_456246514')
        		elif "четверг" in request:
        			write_img(event.user_id, 'photo294605837_456246512')
        		elif "пятница" in request:
        			write_img(event.user_id, 'photo294605837_456246509')
        		else:
        			write_img(event.user_id, 'photo294605837_456246511')



