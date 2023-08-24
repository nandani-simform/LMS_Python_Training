import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data= {}
    header = {'content-Type': 'application/json'}

    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=header, data = json_data)
    data = r.json()
    print(data)

get_data()
 
def post_data():
    data = {
        'name': 'bunny',
        'roll': 121,
        'city': 'mumbai'
    }

    header = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=header, data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 9,
        'name': 'someone',
        'city': 'Baroda',
        'roll': 147,
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)
    data = r.json()
    print(data)
    
# update_data()

def delete_data():
    data = {'id':13}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)
    data = r.json()
    print(data)
    
# delete_data()



