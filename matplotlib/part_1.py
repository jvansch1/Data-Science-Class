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

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axes1.plot(x, y)
axes2.plot(y, x)
axes2.set_title("Inverse")
plt.show()
