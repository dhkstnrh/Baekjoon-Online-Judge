
N = int(input())

first = []
second = []
result = []

for i in range(0, N):
    A, B = map(int, input().split())
    first.append(A)
    second.append(B)
    result.append(A + B)

for j in range(0, N):
    print("Case #{}: {} + {} = {}" .format(j + 1, first[j], second[j], result[j]))
    
