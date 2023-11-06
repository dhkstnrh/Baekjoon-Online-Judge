첫 번째 방법
while True:
    first, second = map(int, input().split())
    try:
        if second % first == 0:
            print('factor')
        elif first % second == 0:
            print('multiple')
        else:
            print('neither')
    except ZeroDivisionError:
        if first == second:
            break


# # 두 번째 방법
# while (1):
#     first, second = map(int, input().split())
#
#     if first == 0 and second == 0:
#         break
#
#     if first < second and second % first == 0:
#         print('factor')
#     elif first > second and first % second == 0:
#         print('multiple')
#     else:
#         print('neither')
