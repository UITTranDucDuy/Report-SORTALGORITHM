import numpy as np
import random
import time

n = int(input())
a = [0]*n
for i in range(n) :
    a[i] = int(input())

a = np.array(a)

start_time = time.time()

a = np.sort(a)

end_time = time.time()

print(a)

elapsed_time_ms = (end_time - start_time) * 1000
print(f"{elapsed_time_ms:.2f}")
