import time
start_time = time.time()

#inner loop
for i in range(10000):
    #outer loop
    for j in range(10):
        print(j ,end=" ")
    print()

print(round((time.time()-start_time),2))