import matplotlib
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t, t, t**2, t, t**3, )
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
xs, ys = np.mgrid[:4, 9:0:-1]
markers = [".", "+", ",", "x", "o", "D", "d", "", "8", "s", "p", "*", "|", "_", "h", "H", 0, 4, "<", "3",
           1, 5, ">", "4", 2, 6, "^", "2", 3, 7, "v", "1", "None", None, " ", ""]
descripts = ["point", "plus", "pixel", "cross", "circle", "diamond", "thin diamond", "",
             "octagon", "square", "pentagon", "star", "vertical bar", "horizontal bar", "hexagon 1", "hexagon 2",
             "tick left", "caret left", "triangle left", "tri left", "tick right", "caret right", "triangle right", "tri right",
             "tick up", "caret up", "triangle up", "tri up", "tick down", "caret down", "triangle down", "tri down",
             "Nothing", "default", "Nothing", "Nothing"]
fig, ax = plt.subplots(1, 1, figsize=(7.5, 4))
for x, y, m, d in zip(xs.T.flat, ys.T.flat, markers, descripts):
    ax.scatter(x, y, marker=m, s=100)
    ax.text(x + 0.1, y - 0.1, d, size=14)
ax.set_axis_off()
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t, t, t**2, t, t**3, )
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t, '-', t, t**2, '--', t, t**3, '-.', t, -t, ':')
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
ax.bar([1, 2, 3, 4], [10, 20, 15, 13], ls='dashed', ec='r', lw=5)
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


import matplotlib
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)
z = np.random.random((10, 10))
ax1.imshow(z, interpolation='none', cmap='gray')
ax2.imshow(z, interpolation='none', cmap='coolwarm')
plt.show()


import matplotlib
import numpy as np
import matplotlib.pyplot as plt

plt.scatter([1, 2, 3, 4], [4, 3, 2, 1])
plt.title(r'$\sigma_i=15$', fontsize=20)
plt.show()


import matplotlib as mpl
from matplotlib.rcsetup import cycler
mpl.rc('axes', prop_cycle=cycler('color', 'rgc') +
                          cycler('lw', [1, 4, 6]) +
                          cycler('linestyle', ['-', '-.', ':']))
t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t)
plt.plot(t, t**2)
plt.plot(t, t**3)
plt.show()


mpl.rc('axes', prop_cycle=cycler('color', ['r', 'orange', 'c', 'y']) +
                          cycler('hatch', ['x', 'xx-', '+O.', '*']))
x = np.array([0.7, 0.3, 0.385, 0.6153, 0.7, np.nan, 0.6, 0.4, 0.2, 0.5, 0.8, 0.6])
y = [0.65, 0.65, 0.1, 0.1, 0.65, np.nan, 0, 0, -5, -6, -5, 0]
plt.fill(x+1, y)
plt.fill(x+2, y)
plt.fill(x+3, y)
plt.fill(x+4, y)
plt.show()


import matplotlib
print(matplotlib.matplotlib_fname())


import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcdefaults()  # for when re-running this cell

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot([1, 2, 3, 4])
mpl.rc('lines', linewidth=2, linestyle='-.')

# Equivalent older, but still valid syntax
#mpl.rcParams['lines.linewidth'] = 2
#mpl.rcParams['lines.linestyle'] = '-.'
ax2.plot([1, 2, 3, 4])
plt.show()
