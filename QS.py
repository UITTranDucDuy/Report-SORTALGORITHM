import random
import time

def hoare_partition(a, low, high):
    pivot = a[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while a[i] < pivot: i += 1
        j -= 1
        while a[j] > pivot: j -= 1
        if i >= j: return j
        a[i], a[j] = a[j], a[i]
    return i + 1

def quick_sort(a, low, high):
    if low < high:
        pi = hoare_partition(a, low, high)
        quick_sort(a, low, pi - 1)
        quick_sort(a, pi + 1, high)


n = int(input())
a = [0]*n
for i in range(n) :
    a[i] = random.randint(1,100000000)
#a.sort()
#a.reverse()

start_time = time.time()

quick_sort(a, 0, len(a) - 1)

end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"{elapsed_time_ms:.2f}")

