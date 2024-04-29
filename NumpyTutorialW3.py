import numpy as np

arr = np.array([10, 2, 3, 4, 5])
arr_string = np.array(("This is a string"), dtype='S')
arr_string2 = np.array(['apple', 'banana', 'cherry'])

arr0D = np.array(55)
arr1D = np.array((1, 2, 3, 4, 5, 6, 7, 8))
arr2D = np.array(((1,2,3), (4, 5, 6), (7, 8, 9)))
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 11, 12], [13, 14, 15]]])
arr5D = np.array([1, 2, 3, 4], ndmin=5)



print(len(arr),"\n")
print(arr,"\n")
print("0D array: ", arr0D,"\n")
print("1D array: ", arr1D,"\n")
print("2D array: ", arr2D, "Dimension: ",arr2D.ndim, "\n")
print("3D array: ", arr3D, "Dimension: ",arr3D.ndim, "\n")
print(arr5D)
print('number of dimensions :', arr5D.ndim, "\n")


# Access to 1D arrays    array [ROW, COLUMN]
print("Access to array element 1: ", arr[0])
print("Acess to 2 elem + addition: ", arr[2] + arr[3])
print("Negative indexing: ", arr[-1])

# Access to 2D arrays    array [ROW, COLUMN]
print("2rd element on 1st row: ", arr2D[0, 1], "\n")

# Access to 3D arrays    array [ROW, COLUMN]
print("3rd element of 2nd array of first array: ", arr3D[0, 1, 2],"\n")

#Slicing. Includes start index but exclude end index
print(arr1D[0::], "----------------",arr2D[0:2, 1], "----------------",arr1D[-3:-1], "\n")
print(arr1D[::2], "\n")
print(arr2D[1, 1::], "\n")
print(arr2D[::, 1:3], "\n")

# Data types in arrays
print(arr1D.dtype)
print(arr_string2.dtype, "\n")

""" COnverting datatype: astype() method
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr_float = np.array([1.1, 2.1, 3.1])
newarr = arr_float.astype('i') # or newarr = arr.astype(int)
newarr_bool = arr.astype(bool)
print(newarr)
print(newarr.dtype, "-----", newarr_bool.dtype, "\n")


# NumPy Array Copy vs View
"""The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

"""
#COPY:
x = arr.copy()
arr[0] = 666
print(arr)
print(x, "\n")

#VIEW:

y = arr.view()
arr[0] = 777
print(arr)
print(y)

#to check if view or copy, use .base attribute, returns NONE if copy
print(x.base)
print(y.base, "\n")


#Shape of an Array, .shape attribute
print(arr2D)
print(arr2D.shape, "\n")

# Reshaping arrays, .reshape attribute

#Convert the 1-D array into a 2-D array:
print(arr1D)
arr2D_new = arr1D.reshape(4,2)
print(arr2D_new, "\n")
#Convert the 1-D array into a 3-D array:
arr3D_new = arr1D.reshape(2,2,2)  #Unknown Dimension, 1 unknown dimmesion allowed with -1: .reshape(2,2,-1)
print(arr3D_new, "\n")

#Flattening arrays (nD->1D), .reshape(-1)
arr1D_new = arr3D.reshape(-1)
print(arr1D_new, "\n")
# Many more fuctions: "flatten, ravel". Also for rearranging the elements "rot90, flip, fliplr, flipud"


# Iterating Arrays
i= 0
while i < (len(arr1D)-1):
    print(arr1D[i], end="--")
    i+=1
print(arr1D[-1])

print("\n")

for x in arr2D:
    for y in x:
        print(y)

print(arr3D)
for x in arr3D:
    for y in x:
        for z in y:
            print(z)

print("\n")

#Iterating Arrays Using nditer()
arr_test = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr_test):
    print(x)
print("\n")

# Iterating Array With Different Data Types    
arr_testi = np.array([1, 2, 3, 4, 5])
for x in np.nditer(arr_testi, flags=['buffered'], op_dtypes=['S']):
    print(x)

#Iterating With Different Step Size
#arr_test = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr2D[:, ::2]):
    print(x)
print("\n")

# Enumerated Iteration Using ndenumerate()
for idx, x in np.ndenumerate(arr2D):
    print(idx, x)
print("\n")

# NumPy Joining Array

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0) # axis= 0: add as rows, axis= 1: add as columns  
arr10 = np.concatenate((arr1, arr2), axis=1)
print(arr)
print(arr10)
print("\n")

#Joining Arrays Using Stack Functions. Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr, "\n")

# Stacking Along Rows. NumPy provides a helper function: hstack() to stack along rows.
arr = np.hstack((arr1, arr2))
print(arr)
#Stacking Along Columns.NumPy provides a helper function: vstack()  to stack along columns.
arr = np.vstack((arr1, arr2))
print(arr)
# Stacking Along Height (depth).NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr = np.dstack((arr1, arr2))
print(arr, "\n")

#NumPy Splitting Array. array_split(). Convert into a list

newarr = np.array_split(arr1D, 3)
print(newarr)
print(newarr[0], "\n")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr2D = np.array_split(arr, 3)
print(newarr2D, "\n")

newarr = np.array_split(arr, 3, axis=1) #Can also use hsplit()
print(newarr)


newarr = np.hsplit(arr, 2)
print(newarr, "\n\n")


# Searching Arrays using where()
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
y = np.where(arr%2==1)
print(y, "\n")

#Search Sorted using searchsorted(), sorting arrays sort()

arr = np.array([5,2,4,1,7,9])
arr = np.sort(arr)
print(arr)
x = np.searchsorted(arr, 3)
print(x)
yy = np.searchsorted(arr, 8, side='right') # not working?
print(yy, "\n")

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x, "\n")

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr), "\n")

#Filtering Arrays. Getting some elements out of an existing array and creating a new array out of them is called filtering.

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr, "\n")

#Create a filter array that will return only values higher than 42:

filter_arr = []
for x in arr:
    if x > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr, "\n")

#Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for x in arr:
    if x%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(newarr, "\n")

# Creating Filter Directly From Array. TRES PUISSANT !!!!
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

