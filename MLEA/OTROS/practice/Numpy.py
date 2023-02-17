import numpy as np
import matplotlib.pyplot as plt

a = np.array([0,1,2,3,4])
a[3:5]=300,350 #must exist at least five elements

a.size
a.ndim # Number of dimensions

# Change to the same value on different indexes
select = [0, 2, 3]
a[select] = 10000
a.mean() # Mean :v
a.std() # standart deviation
a.max()
a.min()

b = np.array([5,4,3,2,1])
print(a+b)
print(a*2)
print(a*b)
print(np.dot(a,b)) #product dot

# secuence from 0 to 2*np.pi using ten values
x = np.linspace(0, 2*np.pi, num=10)
y = np.linspace(0, 2*np.pi, num=10)
print(2*np.pi)
print(x)

plt.plot(x, y)

"""
## Exercise: A bit of everything
Create a Python function from scratch that takes a dataframe and normalises its columns. The function should take an optional argument that allows the user to choose between two options: `'standard'`, which removes column means and divides by their standard deviation, or `'scale'`, which scales columns to a range between 0 and 1 (column minimum values become 0 and column maximum values become 1). The function returns the normalised dataframe. Test your function with the `TopSellingAlbums.csv` CSV file that we used before.
"""