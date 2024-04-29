import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Generate Random Number random.randint()

""" 
i=0
while i<50:
    x = np.random.randint(100)
    print(x)
    i+=1 

#Generate Random Float between 0 and 1: random.rand()

y = np.random.rand()
print(y)

# Generate Random Array random.randint(range, size=(number of elements))

# 1D array of size 5, rand ints between 0-10
x = np.random.randint(10, size=(5))
print(x)

#2D array of size 3x5, numbers 0-50
x = np.random.randint(50, size=(3, 5))
print(x)

# Floats, rand()

#Generate a 1-D array containing 5 random floats:
x = np.random.rand(5)
print(x)

#Generate a 2-D array containing 4*5 random floats between 0-10:
x = 10*np.random.rand(4,5)
print(x)

#Generate Random Number From Array choice()
#The choice() method also allows you to return an array of values.Add a size parameter to specify the shape of the array.
x = np.random.choice([0, 2, 4, 6], size=(3, 5))
print(x)

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9, with a p of 0.1, 0.3, 0.6, 0.0 respectively. 
# Check each proba and sum
x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0],size=(100))
print(x)
sum = 0
for elem in [3, 5, 7, 9]:
    print(f"{elem} appears {np.count_nonzero(x==elem)} times")   
    sum += np.count_nonzero(x==elem)
print("This number should be 100:", sum)

# Random Permutations of Elements shuffle() and permutation()

# The shuffle() method MAKES changes to the original array.
arr = np.array((1,2,3,4,5,6))
np.random.shuffle(arr)
print(arr)

# The permutation() method RETURNS a re-arranged array (and leaves the original array un-changed).

arr = np.array((1,2,3,4,5,6))
print(np.random.permutation(arr))

# Seaborn Module

# Plotting a Distribution plot
sns.distplot([1,2,3,4], hist=False)
plt.show()

#Normal (Gaussian) Distribution random.normal()
It has three parameters:
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array."""

x = np.random.normal(loc=1, scale=2, size=(3,5))
print(x)

sns.distplot(np.random.normal(size=500, loc=3, scale=0.5), hist=False)
plt.show()