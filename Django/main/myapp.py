""" 
    myapp.py -- 3rd party application hai jo andriod /ios/ java kisi ka bhi ho skta h 
    jisse pata pade ki request kha bhejni hai ore response kha GET krna h

    fir file run krni h 
    python myapp.py
"""
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data= {}
    header = {'content-Type': 'application/json'}

    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)  #python to json
    r = requests.get(url=URL, headers=header, data = json_data)
    data = r.json()
    print(data)

get_data()
   
def post_data():
    data = {
        'name': 'aditi',
        'roll': 69,
        'city': 'manali'
    }
    header = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=header, data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 11,
        'name':'Sohan',
        'roll': 131,
        'city': 'Goa',

    }
    header = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=header, data = json_data)
    data = r.json()
    print(data)
    
# update_data()

def delete_data():
    data = {'id':8}
    header = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=header, data = json_data)
    data = r.json()
    print(data)
    
# delete_data()



