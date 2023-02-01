import sys
sys.stdin = open("input.txt")
N = 100
for t in range(10):
    T = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    total_lst = []
    for y in range(N): # 행 검증
        sum = 0
        for x in range(N):
            sum += lst[y][x]
        total_lst.append(sum)

    for x in range(N): # 열 검증
        sum = 0
        for y in range(N):
            sum += lst[y][x]
        total_lst.append(sum)

    sum = 0
    for x in range(N): # 대각선 검증
        sum += lst[x][x]
    total_lst.append(sum)

    sum = 0
    for x in range(N): # 대각선 검증
        sum += lst[x][N-1-x]
    total_lst.append(sum)

    ans = max(total_lst)
    print(f'#{T} {ans}')

        




    
