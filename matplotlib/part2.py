# FROM: https://github.com/matplotlib/AnatomyOfMatplotlib/blob/master/AnatomyOfMatplotlib-Part2-Plotting_Methods_Overview.ipynb

"""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(1)
x = np.arange(5)
y = np.random.randn(5)

fig, axes = plt.subplots(ncols=2, figsize=plt.figaspect(1./2))

vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')

# I'll also introduce axhline & axvline to draw a line all the way across the axes
# This can be a quick-n-easy way to draw an axis "spine".
axes[0].axhline(0, color='gray', linewidth=2)
axes[1].axvline(0, color='gray', linewidth=2)

plt.show()

fig, ax = plt.subplots()
vert_bars = ax.bar(x, y, color='lightblue', align='center')

# We could have also done this with two separate calls to `ax.bar` and numpy boolean indexing.
for bar, height in zip(vert_bars, y):
    if height < 0:
        bar.set(color='salmon', edgecolor='darkred', linewidth=3)

plt.show()

np.random.seed(1)
y = np.random.randn(100).cumsum()
x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()
ax.fill_between(x, y, color='lightblue')
plt.show()

x = np.linspace(0, 10, 200)
y1 = 2 * x + 1
y2 = 3 * x + 1.2
y_mean = 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1

fig, ax = plt.subplots()

# Plot the envelope with `fill_between`
ax.fill_between(x, y1, y2, color='yellow')

# Plot the "centerline" with `plot`
ax.plot(x, y_mean, color='black')

plt.show()

x = np.linspace(0, 10, 200)
data_obj = {'x': x,
            'y1': 2 * x + 1,
            'y2': 3 * x + 1.2,
            'mean': 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1}

fig, ax = plt.subplots()

# Plot the envelope with `fill_between`
ax.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)

# Plot the "centerline" with `plot`
ax.plot('x', 'mean', color='black', data=data_obj)

plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

# Generate data...
y_raw = np.random.randn(1000).cumsum() + 15
x_raw = np.linspace(0, 24, y_raw.size)

# Get averages of every 100 samples...
x_pos = x_raw.reshape(-1, 100).min(axis=1)
y_avg = y_raw.reshape(-1, 100).mean(axis=1)
y_err = y_raw.reshape(-1, 100).ptp(axis=1)

bar_width = x_pos[1] - x_pos[0]

# Make a made up future prediction with a fake confidence
x_pred = np.linspace(0, 30)
y_max_pred = y_avg[0] + y_err[0] + 2.3 * x_pred
y_min_pred = y_avg[0] - y_err[0] + 1.2 * x_pred

# Just so you don't have to guess at the colors...
barcolor, linecolor, fillcolor = 'wheat', 'salmon', 'lightblue'

# Now you're on your own!



fig, ax = plt.subplots()
ax.set_title("Future Projection of Attitudes")
ax.set_xlabel("Minutes Since class began")
ax.set_ylabel("Snarkiness (snark units)")
ax.set_xlim(0, 30)
ax.set_ylim(0, 100)

ax.fill_between(x_pred, y_min_pred, y_max_pred, color=fillcolor)

ax.plot(x_raw, y_raw, color=linecolor)
ax.bar(x_pos, y_avg, bar_width, color=barcolor, edgecolor="grey", yerr=y_err, ecolor="grey", capsize=5, align="edge")


# ax.axhline(y=0, color='gray', linewidth=2)
# ax.axvline(x=0, color='gray', linewidth=2)

plt.show()

print("​")