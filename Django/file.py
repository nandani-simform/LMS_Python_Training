import json


file = open("temp.txt","r")

x = file.read()

# pythondata = json.loads(x)
# print(type(pythondata))

jsondata = json.dumps(x, indent=4)
print(jsondata)
print(type(jsondata))
