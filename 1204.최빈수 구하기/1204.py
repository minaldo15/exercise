import sys
import collections
from collections import Counter
sys.stdin = open("input.txt")



T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    c = Counter(lst) 
    order = c.most_common()
    # print(order)
    maximum = order[0][1]

    num_lst = []
    for num in order:
        if num[1] == maximum:
            num_lst.append(num[0])
    # print(num_lst)
    if len(num_lst) > 1:
        ans = max(num_lst)
    else:
        ans = num_lst[0]

    print(f'#{N} {ans}')

