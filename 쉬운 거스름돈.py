import sys
sys.stdin = open('input.txt', 'r')

money = [50000,10000,5000,1000,500,100,50,10]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    i = 0
    while i < 8:
        lst.append(N//money[i])
        N = N - (money[i]*(N//money[i]))
        i += 1
    print(f'#{tc}')
    print(*lst)


