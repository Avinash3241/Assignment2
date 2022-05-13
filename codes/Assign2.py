
import numpy as np
a = np.array([[1,1,1],[2,5,7],[2,1,-1]])
b = np.array([9,52,0])
c = np.linalg.solve(a,b)
print("x = 1/",c[0])
print("y = 1/",c[1])
print("z = 1/",c[2])