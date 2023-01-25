
A, B, C = map(int, input().split())
D = int(input())

# 최종 초
C1 = (C + D) % 60
B1 = (C + D) // 60

# 최종 분
B2 = (B + B1) % 60
A1 = (B + B1) // 60

# 최종 시
A2 = (A + A1) % 24


print(A2, B2, C1)

