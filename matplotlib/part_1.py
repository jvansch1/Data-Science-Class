import matplotlib.pyplot as plt
import numpy as np
# plt.show() after examples

# create 2 arrays
x = np.linspace(0, 5, 11)
y = x ** 2

# FUNCTIONAL method

# must do show on separate line
# plt.plot(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Simple Example")
#
# plt.subplot(1, 2, 1)
# plt.plot(x, y, "r")
#
# plt.subplot(1, 2, 2)
# plt.plot(y, x, "b")
# plt.show()

# OOP

# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel("X")
# axes.set_ylabel("Y")
# axes.set_title("Title")
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes1.plot(x, y)
# axes2.plot(y, x)
# axes2.set_title("Inverse")
# plt.show()

# fig, axes = plt.subplots(nrows=1, ncols=2)
# axes[0].plot(x,y)
# axes[0].set_title("First Plot")
# axes[1].plot(y,x)
# axes[1].set_title("Second Plot")
# plt.show()

# fig = plt.figure(figsize=(8, 5), dpi=100)
# ax = fig.add_axes([0.1, 0.1, 0.8,0.8])
# ax.plot(x, y)
# plt.show()

# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 5))
#
# axes[0].plot(x, y)
# axes[1].plot(y, x)
# plt.show()

# to save a fig

# fig.savefig('my_figure.png')

# Add a legend

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, x ** 2, label="X squared")
# ax.plot(x, x ** 3, label="X cubed")
#
# ax.legend(loc=0)
# plt.show()

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y, color="#FF8C00", linewidth=3, alpha=1, linestyle=":", marker="o", markersize=10, markerfacecolor='purple', markeredgewidth=3, markeredgecolor='black')
# plt.show()

# Only show between 0 and 1

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y, color='purple', lw=2, ls='--')
ax.set_xlim([0,1])
ax.set_ylim([0,2])
plt.show()
