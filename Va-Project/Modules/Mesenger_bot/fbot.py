import getpass
import fbchat
from fbchat.models import *
import time
counter = 1

client = fbchat.Client(input('Username: '), getpass.getpass())
friends = client.searchForUsers(input('Who do you want to message? '))
friend_id = friends[0].uid
word = str(input('Message: '))
delay = float(input('Delay between each message: '))
msg_count = int(input('How many times do you want the message to be sent?: '))


for i in range(msg_count):
    client.send(Message(text=word), thread_id=friend_id, thread_type=ThreadType.USER)
    print(counter, f"Sending:", word)
    counter = counter+1
    time.sleep(delay)

