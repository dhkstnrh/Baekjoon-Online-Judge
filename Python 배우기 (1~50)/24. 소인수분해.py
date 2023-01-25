N = int(input())

D = 2

while N >= D:
    if N % D == 0:
        print(D)
        N = N / D
    else:
        D += 1