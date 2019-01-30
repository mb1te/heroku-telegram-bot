import vk_api
import math
import random
from settings import *
from data import *
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id' : user_id, 'message' : message, 'random_id': random.randint(1, 10**12)})

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if "расписание звонков" in request:
                write_msg(event.user_id, schedule)