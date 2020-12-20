ques_files = open('question.txt','r')
ques_list = [question.strip () for question in ques_files.readlines()]
ques_files.close()

correct_answer = 0

for question in ques_list:
    pos = question.find('=')+1
    user_ans = input(question[:pos])
    if user_ans == question[pos]:
        correct_answer = correct_answer + 1
report = f'your final grade is {correct_answer} {len(ques_list)}'
result = open('result.txt', 'w')
result.write(report)
result.close()
