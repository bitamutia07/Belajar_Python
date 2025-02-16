#JSON banyak ditemukan jika bermain dengan web serice atau RESTful API 

import json
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])