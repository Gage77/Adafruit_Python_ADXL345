import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):
    xs.append(random.randint(1,10))
    ys.append(random.randint(-10, 10))

    # Limit x and y lists to 20 times
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.3)
    plt.title('Testing dynamic plotting')
    plt.ylabel('New point')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()