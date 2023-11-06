# N = int(input())
# V = []

# for i in range(N):
#     T = int(input())
#     V.append(T)

# CUTE = V.count(1)
# NOT_CUTE = V.count(0)

# if CUTE > NOT_CUTE:
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")
    
    
# 다른 방법
N = int(input())
CUTE = 0
NOT_CUTE = 0

for i in range(N):
    V = int(input())
    if V == 1:
        CUTE += 1
    else:
        NOT_CUTE += 1

if CUTE > NOT_CUTE:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
    
    