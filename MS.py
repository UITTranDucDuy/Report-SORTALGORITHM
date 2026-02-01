import time
import random

def mg_sort(a):
    if len(a) <= 1:
        return a

    m = len(a) // 2
    l_half = a[:m]
    r_half = a[m:]

    l_half = mg_sort(l_half)
    r_half = mg_sort(r_half)

    return merge(l_half, r_half)

def merge(l, r):
    res = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    res.extend(l[i:])
    res.extend(r[j:])

    return res

n = int(input())
a = [0]*n
for i in range(n) :
    a[i] = int(input())

#a.sort();
#a.reverse();

start_time = time.time()

mg_sort(a)

end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"{elapsed_time_ms:.2f}")
