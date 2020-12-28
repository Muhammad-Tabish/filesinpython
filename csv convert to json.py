import json
with open('csv_file.txt', 'r') as file_operate:
    file_convert = [line.strip() for line in file_operate.readlines()]


result = []
for line in file_convert:
    a = line.split(',')
    dict = {"club": a[0],"country": a[2], "city":a[1]}
    result.append(dict)

with open('json_file.txt', 'w') as file_open:
    file_open.write(json.dumps(result))


