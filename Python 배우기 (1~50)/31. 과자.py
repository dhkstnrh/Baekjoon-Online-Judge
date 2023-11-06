
# 과자 한 개의 가격 K
# 사려고 하는 과자의 개수 N
# 현재 OO가 가진 돈 M

K, N, M = map(int, input().split())

P = (K * N) - M

if P > 0:
    print(P)
else:
    print(0)
