T = int(input())

reward = []

for i in range(T):
    A, B, C = map(int, input().split())
    
    if A == B == C:
        reward.append(10000 + (A * 1000))
    elif A == B or A == C:
        reward.append(1000 + (A * 100))
    elif B == C:
        reward.append(1000 + (B * 100))
    elif A != B != C:
        reward.append(max(A, B, C) * 100)


print(max(reward))
