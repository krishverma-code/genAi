import numpy as np # np is the convention to name numpy library..

a = np.array([1,2,3])
print(a)
print(a.shape) # shape operator tells the dimensins of the array in a tuple...
print(a.dtype) # dtype represents dimesion type of an array if it is a mix of elementType it generalises the array type..

b = np.array([[1,2,3] , [4.5,5,6]])
print(b)
print(b.shape)
print(b.dtype) # float is a more general type of dimension than int... 

#for initialising a random array ...(np.zeroes(shape))..by defualt float type (0.)
z = np.zeros((3,4)) 
o = np.ones((2,2))
r = np.arange(0,10,2) # (start , stop , step).. same like range() in python 
print(z)
print(o)
print(r)

l = np.linspace(0,1,5) #.linspace(start , stop , num)
 # gives you 'num' evenly spaces values between start and stop inclusive of both end points..
print(l)

rand = np.random.rand(3,3) # for printing random numbers....np.random.rand(shape)...
print(rand)

c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(c[1,2]) #indexing of an numpy array...(start:end:step),,,end is exclusive...
#this represents [row,column] .. 

print(c[:,2])  #imp--this tells to print every element in 2nd column...

print(c[0:2, 1:3]) #this prints 0th and 1th index element of row and 1st and 2nd index element of columns...
#always gives the answer in flattened array no matter the shape of original array ...

print(c[c % 2 == 0 ]) # this is boolean masking which prints only thosse elements in c array which satisfy this condition...
c[0,:] = 1 # this sets every element of 0th row to 1...
# this change also affects the orginal array..

print(c)

x = np.arange(24)
i = x.reshape(4,6) # changes the shape of this array(shape)..
j = x.reshape(2,3,4) # a 3D matrix of form (blocks,rows,columns)..
k = x.reshape(-1,8) # wherever -1 is present it automatically realigns the shape of matrix according to the number of elements present...

e = a.T # .T represents the transpose of the matrix...

f = a.flatten() # this flattens a 2d or 3d matrix into 1d matrix...

# some utility functions...

a = np.array([1, 2, 3, 4, 5])

print(np.sum(a))       # 15      -> sum of all elements
print(np.mean(a))      # 3.0     -> average
print(np.max(a))       # 5       -> maximum value
print(np.min(a))       # 1       -> minimum value
print(np.argmax(a))    # 4       -> INDEX of maximum value (not the value itself)
print(np.argmin(a))    # 0       -> INDEX of minimum value

# On 2D arrays, you can specify axis:
b = np.array([[1, 5, 3], [4, 2, 6]])
print(np.sum(b, axis=0))   # [5 7 9]  -> sum each column (collapse rows)
print(np.sum(b, axis=1))   # [9 12]   -> sum each row (collapse columns)



