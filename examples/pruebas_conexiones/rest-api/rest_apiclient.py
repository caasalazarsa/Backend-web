# client.py

import requests
import json

#url = 'http://localhost:5000/todo/api/v1.0/tasks'
url = 'https://ffd0-190-60-223-122.ngrok-free.app/todo/api/v1.0/tasks'

response = requests.get(url)

print(str(response))
print('')
print(json.dumps(response.json(), indent=4))


#url2 = 'http://localhost:5000/todo/api/v1.0/createtask'
url2 = 'https://ffd0-190-60-223-122.ngrok-free.app/todo/api/v1.0/createtask'

myobj={
        'id': 4,
        'title': u'Calificar PIA',
        'description': u'Revisar video, logo, eslogan y excel',
        'done': False

    }

response = requests.post(url2,json=myobj)

print(str(response))
print('')
print(json.dumps(response.json(), indent=4))