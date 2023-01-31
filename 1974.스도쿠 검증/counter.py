import collections
from collections import Counter
N = 'misisipi'
cnt_N = Counter(N)
com_N = cnt_N.most_common(1)
print(cnt_N)
print(com_N[0][1])