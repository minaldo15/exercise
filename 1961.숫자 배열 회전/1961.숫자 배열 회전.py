f = open('input.txt')
input = f.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    origin = []
    for n in range(N):
        row = list(map(int,input().split()))
        origin.append(row)
    # print(origin)

    lst_90 = []
    for y in range(N):
        row = []
        for x in range(N):
            row.append(origin[N-1-x][y])
        lst_90.append(row)
    # print(lst_90)

    lst_180 = []
    for y in range(N):
        row = []
        for x in range(N):
            row.append(lst_90[N-1-x][y])
        lst_180.append(row)
    # print(lst_180)

    lst_270 = []
    for y in range(N):
        row = []
        for x in range(N):
            row.append(lst_180[N-1-x][y])
        lst_270.append(row)
    # print(lst_270)

    print(f'#{t}')
    for n in range(N):
        print(f"{''.join(map(str, lst_90[n]))} {''.join(map(str, lst_180[n]))} {''.join(map(str, lst_270[n]))}")
