import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = []
    stk = []
    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                stk.append(j)
                if j == n-1:
                    if stk:
                        lst.append(stk[-1]-stk[0]+1)
                        stk.clear()
            else:
                if stk:
                    lst.append(stk[-1]-stk[0]+1)
                    stk.clear()
    for num in lst:
        a = lst.count(num)
        if (a, num) not in stk:
            stk.append((a, num))
    stk.sort(key = lambda x:(x[0]*x[1], x[0]))
    ans.append(len(stk))
    for tup in stk:
        ans.append(tup[0])
        ans.append(tup[1])
    print(f'#{tc}', *ans)







