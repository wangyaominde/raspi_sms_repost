import requests
app_token = 'app token'
user_token = 'user token'
title = 'TEST MESSGAE'
text = 'text for polling'
params = {
            'token': app_token,
            'user': user_token,
            'title': title,
            'message': text,
            'retry': 30, 
            'expire': 180,
            'priority': 2,
            'sound': 'siren',
        }
msg = requests.post('https://api.pushover.net/1/messages.json', data=params)
print("POSTed message")
print(msg.json())