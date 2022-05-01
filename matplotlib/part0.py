# FROM: https://github.com/matplotlib/AnatomyOfMatplotlib/blob/master/AnatomyOfMatplotlib-Part0-Intro2NumPy.ipynb

import numpy as np

a = np.array([1, 2, 3])
print(a.shape)
print(a.size)
print(a.ndim)

x = np.arange(100)
print(x.shape)
print(x.size)
print(x.ndim)

y = np.random.rand(5, 80)
print(y.shape)
print(y.size)
print(y.ndim)

x.shape = (20, 5)
print(x)

y.shape = (4, 20, -1)
print(y.shape)


# Scalar Indexing
print(x[2])

# Slicing
print(x[2:5])

# Advanced slicing
print("First 5 rows\n", x[:5])
print("Row 18 to the end\n", x[18:])
print("Last 5 rows\n", x[-5:])
print("Reverse the rows\n", x[::-1])

# Boolean Indexing
print(x[(x % 2) == 0])

# Fancy Indexing -- Note the use of a list, not tuple!
print(x[[1, 3, 8, 9, 2]])

print("Shape of X:", x.shape)
print("Shape of Y:", y.shape)

a = x + y
print(a.shape)
b = x[np.newaxis, :, :] + y
print(b.shape)
c = np.tile(x, (4, 1, 1)) + y
print(c.shape)
print("Are a and b identical?", np.all(a == b))
print("Are a and c identical?", np.all(a == c))

x = np.arange(-5, 5, 0.1)
y = np.arange(-8, 8, 0.25)
print(x.shape, y.shape)
z = x[np.newaxis, :] * y[:, np.newaxis]
print(z.shape)

# More concisely
y, x = np.ogrid[-8:8:0.25, -5:5:0.1]
print(x.shape, y.shape)
z = x * y
print(z.shape)

