friends = input('Enter the Friend Name: ').split(',')
file_content = open('people.txt', 'r')
people_nearby = [line.strip() for line in file_content.readlines()]

file_content.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_Set = friends_set.intersection(people_nearby_set)
nearby_friends_file = open('nearby_friends.txt','w')
for friend in friends_nearby_Set:
    print(f'{friend} is nearby')
    nearby_friends_file.write(f'{friend}/n')
nearby_friends_file.close()

