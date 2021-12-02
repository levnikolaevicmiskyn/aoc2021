import numpy as np

x = np.fromfile('input.txt',dtype=int,sep='\n')

count = sum(x[1:]-x[0:-1] > 0)
print(x[1:]-x[0:-1] > 0)
print('Number of hits: {count}'.format(count=count))
