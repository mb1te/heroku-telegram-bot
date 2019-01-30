import vk_api
import math
import random
from vk_api.longpoll import VkLongPoll, VkEventType

token = '636b5ca075a225c1ae9ae8f36071ea8b1e3a562aab156c4c2095ead56ea3a16d251ccd708f2197eccd755'

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id' : user_id, 'message' : message, 'random_id': random.randint(1, 10**12)})

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if "#factorial " in request:
                s = request.split()
                write_msg(event.user_id, str(math.factorial(int(s[1]))))
            else:
                write_msg(event.user_id, "sorry")