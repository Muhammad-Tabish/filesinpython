csv_files = open('csv_data.txt', 'r')
files =  csv_files.readlines()
csv_files.close()

files = [line.strip() for line in files [1:]]
for line in files:
    personal_data = line.split(',')
    name = personal_data[0].title()
    age = personal_data[1]
    university = personal_data[2].title()
    degree = personal_data[3].capitalize()
    print(f'{name} is {age}, studying {degree} at {university}.')


sample_csv_value = ':'.join(['Rolf', '25', 'MIT', 'computer science'])
print(sample_csv_value)