import collections
from collections import Counter

f = open('input.txt')
input = f.readline

T = int(input())
for t in range(1, T + 1):
    flag = 1
    t_case = []
    for row in range(1, 10):
        t_case.append(list(map(int, input().split()))) # 각 t마다 t_case만들기

    for row in t_case: # 행 검증
        cnt_row = Counter(row)
        com_row = cnt_row.most_common(1)        
        if com_row[0][1] > 1:
            flag = 0
        else:
            pass
    
    for i in range(9): # 열 검증 i는 1~9
        col_lst = []
        for row in t_case: 
            col_lst.append(row[i]) # 각 열리스트(col_lst)에 각 행(row)에서 i번째 숫자 추가 
        cnt_col = Counter(col_lst)
        com_col = cnt_col.most_common(1)        
        if com_col[0][1] > 1:
            flag = 0
        else:
            pass

    # 정사각형 검증 추가
    
    for k in range(3):
        # (0,0)~(2,2) ~~~ (6,0)~(8,2)
        square_lst = []
        for i in range(3):
            for j in range(3):
                square_lst.append(t_case[i][j+(3*k)])
        # print(square_lst)
        cnt_square = Counter(square_lst)
        com_square = cnt_square.most_common(1)        
        if com_square[0][1] > 1:
            flag = 0
        else:
            pass
    

    for k in range(3):
        # (0,0)~(2,2) ~~~ (6,0)~(8,2)
        square_lst = []
        for i in range(3):
            for j in range(3):
                square_lst.append(t_case[i+3][j+(3*k)])
        # print(square_lst)
        cnt_square = Counter(square_lst)
        com_square = cnt_square.most_common(1)        
        if com_square[0][1] > 1:
            flag = 0
        else:
            pass

    for k in range(3):
        # (0,0)~(2,2) ~~~ (6,0)~(8,2)
        square_lst = []
        for i in range(3):
            for j in range(3):
                square_lst.append(t_case[i+6][j+(3*k)])
        # print(square_lst)
        cnt_square = Counter(square_lst)
        com_square = cnt_square.most_common(1)        
        if com_square[0][1] > 1:
            flag = 0
        else:
            pass


    if flag == 1:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')