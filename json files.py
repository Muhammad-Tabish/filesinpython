import json

file = open('friends_json.txt', 'r')
file_content = json.load(file)
file.close()

print(file_content['friends'][0])