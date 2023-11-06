
A, B = map(int, input().split())
C = 45

B -= C % 60

if B < 0:
    A -= 1
    B += 60

if A >= 24:
    A -= 24

if A < 0:
    A += 24


print(A, B)

