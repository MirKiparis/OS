import time


a=0
b=3
c=3
noIterations = 100000000
start_time = time.time()
for i in range(noIterations):
    a += b*2 + c - i

print((time.time() - start_time)*1000, ' ms')
