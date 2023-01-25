# 이게 내가 푼거
"""
T = int(input())


for i in range(T):
    R, S = list(map(str, input().split()))
    T_R = int(R[0])
    result = []
    
    for j in range(len(S)):
        T_S = T_R * S[j]
        result.append(T_S)
        str1 = ''.join(result)
    
    print(str1)

"""

# 다른 사람이 푼거
T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    
    for j in S:
        print(j * R, end = "")
    print()

