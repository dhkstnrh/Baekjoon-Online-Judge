N = int(input())

Q1, Q2, Q3, Q4, Axis = 0, 0, 0, 0, 0

for i in range(N):
    X, Y = map(int, input().split())
    if X > 0 and Y > 0:
        Q1 += 1
    elif X < 0 and Y < 0:
        Q3 += 1
    elif X < 0 and Y > 0:
        Q2 += 1
    elif X > 0 and Y < 0:
        Q4 += 1
    else:
        Axis += 1

print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {Axis}')