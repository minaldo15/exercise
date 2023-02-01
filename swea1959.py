import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    K = abs(N - M) + 1
    if N < M:
        t_lst = []
        for k in range(K):
            sum = 0
            for i in range(N):
                sum += (A[i] * B[i+k])
            t_lst.append(sum)
        ans = max(t_lst)
    else:
        t_lst = []
        for k in range(K):
            sum = 0
            for i in range(M):
                sum += (A[i+k] * B[i])
            t_lst.append(sum)
        ans = max(t_lst)
    print(f'#{t} {ans}')


