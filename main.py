__copyright__ = '@nirocoder'
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.sync import TelegramClient
from telethon import connection
from telethon import events
from pprint import pprint
import random
import time
import os


if os.path.exists('photo1.jpg'):
    os.remove('photo1.jpg')

api_id = 'You have to get your api_id!'
api_hash = 'Your api_hash, you can get it from site my.telegram.org!'

client = TelegramClient(
    'session', 
    api_id, 
    api_hash,
    # proxy=(type, "host", port) if u wanna use proxy u can set it 
)

client.start()


def del_exist_file() -> bool:
    if os.path.exists('photo1.jpg'):
        os.remove('photo1.jpg')
        return True
    else:
        return False

        
def main():
    channel_username = 't.me/belial_black_foto' # It's channel where a lot of photos for this script
    messages = client.get_messages(channel_username, limit=500) # You can set ur message limit
    try:
        while True:
            try:
                ran_message = random.choice(messages)
                if ran_message.photo != None:
                    ran_message.download_media(file=os.path.join('', f'photo1'))
                    file = client.upload_file('photo1.jpg')
                    client(DeletePhotosRequest(client.get_profile_photos('me')))
                    client(UploadProfilePhotoRequest(file=file))
                    del_exist_file()
                    time.sleep(7)
                else:
                    print("[!] Another type of message")
                    continue
            except Exception as e:
                print(e)
                del_exist_file()
                continue
    except Exception as e: # We have to always catch errors and handle them!
        print(e)
        del_exist_file()


if __name__ == '__main__':
    try:
        print('[!] started')
        main()
    except Exception as e:
        print("[!] error: " + str(e))
        del_exist_file()
        
