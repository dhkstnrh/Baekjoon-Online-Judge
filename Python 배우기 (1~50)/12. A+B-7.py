
# N = int(input())
# result = []

# for i in range(0, N):
#     A, B = map(int, input().split())
#     result.append(A + B)

# for j in range(0, N):
#     print("Case #{}: {}" .format(j+1, result[j]))
    
N = int(input())

for i in range(1, N+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a + b}')