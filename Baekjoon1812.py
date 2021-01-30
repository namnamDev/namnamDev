## 1 2 3 4 1
## 1 3 5 7
##  4 8 12 8
#a(N-1) = 합-a(N-2)
T = int(input())
students_has = []
students = []
for case in range(T) :
    students_has.append(int(input()))

sums = 0
for cases in range(T):
    if cases%2 :
        sums -= students_has[cases]
    else :
        sums += students_has[cases]

students.append(sums//2)
print(students[0])
for i in range(0,T-1):
    students.append(students_has[i]-students[i])
students.pop(0)
for i in students :
    print(i)


## 5 7 6 
## 1 2 3 1
## 2 3 4 2
## 
## a(1) = st[0] -a(2)
## a(1) = st[0] -(stu[1]-a(3)) 
#       = st[0] - ((stu[1] - (stu[2]-a1)) 
#       = st[0] - stu[1] + stu[2] - a(1)
#       = st[0] - stu[1] +stu[2] -a1 
#       = (st[0] - stu[1] +stu[2])//2
## a(2) = students_has[1] -a(3)
## a(3) = students_has[2] -a(1)
#
#1 2 3 4 5 1
#2 3 4 5 6 2
# 5 7 9 11 8 
#a(1) = st[0] -(stu[1]-a(3))
#a(1) = st[0] -(stu[1]-(stu[2]-a4))
#a(1) = st[0] -(stu[1]-(stu[2]-(st[3]-a(1))))
#a(1) = st[0] -stu[1]+stu[2]-st[3]++st[4] - a(1)
#a(1) = (st[0] -stu[1]+stu[2]-st[3]+st[4])//2