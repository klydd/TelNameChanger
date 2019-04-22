from telethon import TelegramClient, sync, functions
from time import sleep
import random

def changes():
    f_name = str()
    l_name = str()
    for i in range (16):
        change = random.randint (1,3)
        if change == 1:
            f_name += chr(random.randint(65,90))
        elif change == 2:
            f_name += chr(random.randint(97,122))
        else:
            f_name += chr(random.randint(36,57))
            
        change = random.randint (1,3)
        if change == 1:
            l_name += chr(random.randint(65,90))
        elif change == 2:
            l_name += chr(random.randint(97,122))
        else:
            l_name += chr(random.randint(36,57))
            
    result = client(functions.account.UpdateProfileRequest(
        first_name = f_name,
        last_name = l_name))

api_id = 12345
api_hash = 'qwerty'

client = TelegramClient('sess_name', api_id, api_hash)
client.start()

while True:
    try:
        changes()
        sleep (40)
    except Exception as e:
        print (e)
    
