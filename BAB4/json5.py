#mencetak mudah data json

from asyncio.windows_events import NULL
import json
person_string = '{ "name": "Bob", "language" : "English","numbers" : [2, 1.6, null]}'

person_dict = json.loads(person_string)
print(json.dumps(person_dict, indent=4, sort_keys=True))