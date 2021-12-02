import numpy as np

x = np.fromfile('input_test.txt', dtype=int, sep='\n')

count = 0
for i in range(len(x)-3):
    if sum(x[i+1:i+4]) > sum(x[i:i+3]):
        count = count+1

print('Count:{count}'.format(count=count))
