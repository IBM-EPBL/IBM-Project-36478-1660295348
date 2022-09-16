import numpy as np
a=np.array([1,2,3])
b=np.array([3,4,5])
n=np.concatenate((a,b), axis = 0)
print(n)
