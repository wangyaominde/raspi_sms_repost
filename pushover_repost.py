import requests
import time
app_token = 'a8wca1ig79pz9ayusuydbz965anb2o'
user_token = 'u7ww9ygiag4p1whmx2dcg9uayo1dn7'
title = 'TEST MESSGAE'
text = 'hello world'
params = {
            'token': app_token,
            'user': user_token,
            'title': title,
            'message': text,
            'retry': 30, 
            'expire': 180,
            'priority': 0,
            'sound': 'Bike',
        }

        
msg = requests.post('https://api.pushover.net/1/messages.json', data=params)
print("POSTed message")
print(msg.json())
