
while True:
    # M은 상근이의 남자 친구의 수
    # F는 상근이의 여자 친구의 수
    M, F = map(int, input().split())

    if M == 0 and F == 0:
        break

    print(M + F)