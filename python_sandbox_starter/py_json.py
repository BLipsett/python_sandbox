# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

userJson = '{"first_name": "John", "last_name": "Doe", "age": 40}'

user = json.loads(userJson)

print(user)

car = { 'make': 'Ford', 'model': 'fiesta', 'year': 2009}

carJSON = json.dumps(car)

print(car['model'])