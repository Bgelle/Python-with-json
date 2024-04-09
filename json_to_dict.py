import json
person='{"name":"vikas","languages":["English","Hindi"],"Tech skills":["cobol","python","java","xml"]}'
person_dict=json.loads(person)
print(person_dict)