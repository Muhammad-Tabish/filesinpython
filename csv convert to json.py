import json
file_operate = open('csv_file.txt', 'r')
file_convert = [line.strip() for line in file_operate.readlines()]

file_operate.close()
result = []
for line in file_convert:
    a = line.split(',')
    dict = {"club": a[0],"country": a[2], "city":a[1]}
    result.append(dict)

file_open = open('json_file.txt', 'w')
file_open.write(json.dumps(result))
file_open.close()

