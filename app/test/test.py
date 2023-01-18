import requests
import json

# Test adding a diver
data = {'diver_id': '1', 'firstName': 'John', 'lastName': 'Doe', 'meter': '3', 'discipline': 'Dynamic', 'time': '100', 'country': 'USA', 'NR': 'Yes', 'gender': 'male'}
r = requests.post('http://app_comp:5001/comp1', data=data)
assert r.status_code == 200

# Test getting a diver
r = requests.get('http://app_comp:5001/comp1')
assert r.status_code == 200
divers = json.loads(r.text)
assert len(divers) == 1
assert divers[0]['firstName'] == 'John'

# Test updating a diver
data = {'firstName': 'Jane'}
r = requests.put('http://app_comp:5001/comp1', data=data)
assert r.status_code == 200
divers = json.loads(r.text)
assert divers[0]['firstName'] == 'Jane'

# Test deleting a diver
r = requests.delete('http://app_comp:5001/comp1/1')
assert r.status_code == 200

# Test getting all divers after deletion
r = requests.get('http://app_comp:5001/comp1')
assert r.status_code == 200
divers = json.loads(r.text)
assert len(divers) == 0

