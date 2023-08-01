"""
01202021,75;01201033,95;01202008,80;01203006,90;01203088,100
01202008,70;01203088,85;01202111,80;01202021,75;01201100,88

找出选了两个课的学生，先按班级划分，班号小的先输出，每个班级按两门课成绩和逆序排列，成绩相同的按学生学号升序排列

01 学院 20入学年 2 院系编号 021 班级学号
"""

s1 = '01202021,75;01201033,95;01202008,80;01203006,90;01203088,100'
s2 = '01202008,70;01203088,85;01202111,80;01202021,75;01201100,88'

'''
01201022,75;01202033,95;01202018,80;01203006,90;01202066,100
01202008,70;01203102,85;01202111,80;01201021,75;01201100,88

'''
s1 = '01201022,75;01202033,95;01202018,80;01203006,90;01202066,100'
s2 = '01202008,70;01203102,85;01202111,80;01201021,75;01201100,88'
student = {}

for line in [s1, s2]:
    row = line.split(';')
    for cell in row:
        number, score = cell.split(',')
        key = (number[:5], number[-3:])

        if key not in student:
            student[key] = [int(score), 1]
        else:
            student[key][0] += int(score)
            student[key][1] += 1

filter_student = []
for key, val in student.items():
    if val[1] == 2:
        filter_student.append((key, val))

if len(filter_student) == 0:
    print("NULL")

# 按班号顺序
res = sorted(filter_student, key=lambda x: x[0][1])


# 按成绩逆序
res = sorted(res, key=lambda x: x[1][1], reverse=True)


student = {}
for row in res:
    if row[0][0] not in student:
        student[row[0][0]] = []
    student[row[0][0]].append(row[0])


for key, val in student.items():
    print(key)
    print(';'.join([''.join(row) for row in val]))

