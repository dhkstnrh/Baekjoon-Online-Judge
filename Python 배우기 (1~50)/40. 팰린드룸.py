# 첫 번째 방법
# word = list(input())

# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)
    
# # 두 번째 방법
# word = input()
# cnt = 0

# for i in range(((len(word) // 2) + 1)):
#     if word[i] != word[-1-i]:
#         cnt += 1
# if cnt == 0:
#     print(1)
# else:
#     print(0)


# 세 번째 방법

word = input()

if word[::-1] == word:
    print(1)
else:
    print(0)