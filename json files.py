import json
file = open('friends_json.txt', 'r')
file_content = json.load(file)
file.close()

print(file_content['friends'][0])


cars = [
    {
        'name': 'ford', 'model': 'fiesta'
    }
]
file_1 = open('cars_json.txt', 'w')
json.dump(cars,file_1)
file_1.close()


inorrect_cars = '[{"name": "limkokwing", "year": 2020}]'
inorrect1_cars = json.loads(inorrect_cars)
print(inorrect1_cars [0] ['name'])