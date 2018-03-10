import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 100)
y = x * 2
z = x ** 2

# exercise 1(plot x, y)

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y)
# ax.set_title("Title")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# plt.show()

# exercise 2(create two sets of axes)
#
# fig = plt.figure()
# ax1 = fig.add_axes([0, 0, 1, 1])
# ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
# ax1.plot(x, y)
# ax2.plot(x, y)
# plt.show()

# exercise 3(create two sets of axes)

# fig = plt.figure()
# ax1 = fig.add_axes([0, 0, 1, 1])
# ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])
# ax1.plot(x, z)
# ax2.plot(x, y)
# ax1.set_ylabel("Z")
# ax1.set_xlabel("X")
# ax2.set_title("Zoom")
# ax2.set_ylabel("Y")
# ax2.set_xlabel("X")
# ax2.set_xlim([20, 22])
# ax2.set_ylim([30, 50])
# plt.show()

# exercise 4(create subplots)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 2))
axes[0].plot(x, y, color='blue', linestyle="--", linewidth=5)
axes[1].plot(x, z, color='red', linewidth=5)
plt.tight_layout()
plt.show()
