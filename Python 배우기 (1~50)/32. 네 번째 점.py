X = []
Y = []

for i in range(3):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)

for j in range(3):
    if X.count(X[j]) == 1:
        result_X = X[j]

    if Y.count(Y[j]) == 1:
        result_Y = Y[j]

print(result_X, result_Y)