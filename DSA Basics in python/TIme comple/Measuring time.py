


# For example print from 1 to 100
import time

start = time.time()
for i in range(0,101):
    print(i)

print(time.time()- start)   # But this is not correct way to measure the time
# Because thie method is dependant on machine you r using . it changes for machine to machine
