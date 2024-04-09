import json
person='{"name":"vikas","languages":["English","Hindi"]}'
person_dict=json.loads(person)
print(person_dict)