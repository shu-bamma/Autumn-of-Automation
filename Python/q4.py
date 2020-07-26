import numpy as np

def eq(x,y):
  assert(x.shape[0] == y.shape[0])
  a=np.linalg.inv(np.dot(x.T,x))
  b=np.dot(a,x.T)
  theta=np.dot(b,y)
  return theta
x=np.random.normal(size=(20,20))

y=np.array(np.random.randn(20,1),dtype='int32')

print(eq(x,y))