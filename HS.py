import time
import random

def heapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[l] > a[largest]:
        largest = l

    if r < n and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]

        heapify(a, i, 0)

n = int(input())
a = [0]*n
for i in range(n) :
    a[i] = int(input())

#a.sort();
#a.reverse();

start_time = time.time()

heap_sort(a)

end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"{elapsed_time_ms:.2f}")
