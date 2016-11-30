import numpy as np
from numpy.linalg import inv

A = np.random.randint(10, size=(2,2))
B = np.random.randint(10, size=(2,2))

print("A")
for row in A:
  print(row)
  
print("B")
for row in B:
  print(row)
  
E = A.transpose()

print("Transpose A")
for row in E:
  print(row)
  
F = B.transpose()

print("Transpose B")
for row in F:
  print(row)
  
ainver = inv(A);

print("inverse A");
for row in ainver:
  print(row)
  
binver = inv(B);

print("inverse B");
for row in binver:
  print(row)