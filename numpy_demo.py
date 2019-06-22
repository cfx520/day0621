import numpy as np
data=np.array([1,3,2,22,14])
#print type(data)
#print dir(data)
#print data.dtype
#new_data=data.astype(np.float)
#print new_data.dtype
#print new_data.ndim
#print np.array()
#a=np.array([2,4,2,1])
#print a
#b=np.array([1,2,3,11],dtype=float)
a=np.array([[1,2,3],[3,2]])
da=np.ones((2,))
#da=np.zeros((2,3))
daa=np.ones(2)
#print da,daa
#print da.shape,daa.shape
#print da.ndim,daa.ndim
#da=6.4*np.ones_like(da)
#print np.full(da.shape,6.4)
my_type=np.dtype({"names":['program','vision'],"formats":['S40',np.int]})
my_books=np.array([('python',2),('java',1.8)],dtype=my_type)
print my_books,my_books.dtype