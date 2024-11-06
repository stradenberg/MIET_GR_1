import json
import random


data = {
    "pon": {
        "id": "274576554589654"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

for x in range(1):
    a = random.randint(1, 45327457655458965435)
    print(a)
    data['id'] = a

print(data)
