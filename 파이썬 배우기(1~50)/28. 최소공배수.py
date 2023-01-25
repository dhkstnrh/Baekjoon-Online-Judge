'''
유클리드 호제법으로 구하기
유클리드 호제법은 두 수의 최대공약수를 구하는 알고리즘
호제법? -> 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘
최소공배수는 A와 B의 곱을 최대약수로 나눈 몫이다.
'''

# 최대공약수 구하기
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
# 최소공배수 구하기
def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result
    
T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    print(lcm(x, y))