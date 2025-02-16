# Membaca file format JSON

import json
with open ('BAB4/person.json') as f :
  data = json.load(f)
  print (data)
