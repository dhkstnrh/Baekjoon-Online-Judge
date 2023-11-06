# 첫 번째 방법

'''SCORE = input()

if SCORE == "A+":
    print(4.3)
elif SCORE == "A0":
    print(4.0)
elif SCORE == "A-":
    print(3.7)

if SCORE == "B+":
    print(3.3)
elif SCORE == "B0":
    print(3.0)
elif SCORE == "B-":
    print(2.7)

if SCORE == "C+":
    print(2.3)
elif SCORE == "C0":
    print(2.0)
elif SCORE == "C-":
    print(1.7)

if SCORE == "D+":
    print(1.3)
elif SCORE == "D0":
    print(1.0)
elif SCORE == "D-":
    print(0.7)

if SCORE == "F":
    print(0.0)

'''

dic = {'A+': '4.3', 'A0': '4.0', 'A-': '3.7',
       'B+': '3.3', 'B0': '3.0', 'B-': '2.7',
       'C+': '2.3', 'C0': '2.0', 'C-': '1.7',
       'D+': '1.3', 'D0': '1.0', 'D-': '0.7',
       'F': '0.0'}
grade = input()

print(dic[grade])

