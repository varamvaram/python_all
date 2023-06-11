# JavaScript object notation.
import json
# some JSON:
details =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
person_detail= json.loads(details)
#the result is a Python dictionary:
print(person_detail["name"])


#import json
# a Python object (dict):
person_detail1= {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
person_detail2= json.dumps(person_detail1)
# the result is a JSON string:
print(person_detail2)
