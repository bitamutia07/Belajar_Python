#menulis data ke file json

import json
person_dict = {
  "name": "Bob",
  "languange": ["English", "Fench"],
  "married": True,
  "age": 32
}

with open ('person.txt', 'w') as json_file :
  json.dump(person_dict, json_file)