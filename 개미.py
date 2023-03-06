import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
si, sj = h - q, p
ci, cj = si, sj
k = 0
di, dj = -1, 1
while k < t%(w*h):
    ni, nj = ci+di, cj+dj
    if ni == 0:
        if nj == w:
            di, dj = -di, -dj
        if nj < w:
            di = -di
    elif nj == 0:
        if ni < h:
            dj = -dj
        if ni == h:
            di, dj = -di, -dj

    elif nj == w and ni > 0:
        dj = -dj
    elif ni == h and nj > 0:
        di = -di
    ci, cj = ni, nj
    k += 1
x, y = nj, h - ni
print(x, y)



