
S = []

for i in range(0, 5):
    A = int(input())   
    if A < 40:
        A = 40
    
    S.append(A)
    
avg =int(sum(S) / 5)

print(avg)
