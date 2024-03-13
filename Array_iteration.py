import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
   print(x)

import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print('Original array is:')
print(a)
print('\n')
print('Transpose of the original array is:')
b = a.T 
print(b) 
print('\n')  
print ('Modified array is:')
for x in np.nditer(b): 
   print(x)
