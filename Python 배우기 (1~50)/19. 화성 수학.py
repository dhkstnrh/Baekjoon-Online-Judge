
T = int(input())


for i in range(T):
    a = list(map(str, input().split()))
    
    # 리스트의 첫 번째 문자열을 result에 저장
    result = float(a[0])
    
    for j in range(len(a)):
        if a[j] == "@":
            result = result * 3
        elif a[j] == "%":
            result = result + 5
        elif a[j] == "#":
            result = result - 7
    
    print("%.2f" % result)
        