# server.py

from flask import Flask, jsonify,redirect, url_for, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': u'Presentar PIA',
        'description': u'Entregar video, logo, eslogan y excel',
        'done': True

    }
]




@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/createtask', methods=['POST'])
def create_task():
    if request.method == 'POST':
      if request.form not in tasks:
         tasks.append(request.get_json())
         print(tasks)
         return jsonify({'response':'Success'})
      
      return jsonify({'response':'Input already present'})

    return jsonify({'response':'Fail'})

if __name__ == '__main__':
    app.run(debug=True)