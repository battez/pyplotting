# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)
x4 = np.random.uniform(0, 6, 10000)

LAST_FRAME = 20

label_template = '{0} ({1}) n={3}'

def update(curr):
    if curr > LAST_FRAME:
        a.event_source.stop()
    bin_power = ((curr + 40) / 20.0)
    bins = int(10 ** bin_power)
    
    # nice way to do multiple at same time
    for x, ax, var_name, var_type in zip(all_x, all_axes, all_label_var, all_label_type):
        ax.cla()
        ax.hist(x, density=True, bins=bins, alpha=1)
        ax.axis([-7,21,0,0.6])
        title = label_template.format(var_name, var_type, bin_power, bins)
        ax.set_title(title)
    
    return all_axes

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)


plt.subplots_adjust(hspace=0.3)

all_x = [x1, x2, x3, x4]
all_axes = [ax1, ax2, ax3, ax4]
all_label_var = ['x1', 'x2', 'x3', 'x4']
all_label_type = ['Normal', 'Gamma', 'Exponential', 'Uniform']

a = animation.FuncAnimation(fig, update, frames=1 + LAST_FRAME, interval=100)

# a.save('w2a1.mp4', fps=5, extra_args=['-vcodec', 'libx264'])
plt.show()
