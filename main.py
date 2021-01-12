my_file = open('utilies/data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)


user_name = input('enter your name')
my_file_writing = open('utilies/data.txt', 'w')
my_file_writing.write(user_name)
my_file_writing.close()

print(my_file_writing)