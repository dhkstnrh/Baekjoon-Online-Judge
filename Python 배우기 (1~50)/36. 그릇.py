
bowl = input()
ans = 10 # 처음 그릇을 바닥에 놓았을 때 높이 10cm

for i in range(1, len(bowl)):
    # 두 번째 그릇부터 이전 그릇과 비교 시작
    if bowl[i] == bowl[i - 1]:
        ans += 5  # 같은 방향이면 5cm 추가
    else:
        ans += 10

print(ans)


