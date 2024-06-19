
# looks like last homework
from collections import defaultdict
progres_list = defaultdict(dict)


while True:
    user_input = input("Введите предмет, фамилию и оценку (нажмите дважды Enter по завершению): ")
    if not user_input:
        break
    
    subject, student, grade = user_input.split()
    
    if student in progres_list[subject]:
        progres_list[subject][student].append(int(grade)) #для группировки по оценкам
    else:
        progres_list[subject][student] = [int(grade)]
    #print(progres_list)

# Выводим результат
for subject, students in progres_list.items():
    print('')
    print(subject)
    for student, grades_list in students.items():
        print(f"{student} {' '.join(map(str, grades_list))}")