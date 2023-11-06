
V = int(input())
vote = list(input())


A_count = vote.count('A')
B_count = vote.count('B')

if A_count > B_count:
    print('A')
elif A_count == B_count:
    print('Tie')
else:
    print('B')

