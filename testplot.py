import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import Adafruit_ADXL345

# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()

fig = plt.figure()
global incrementor
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

incrementor = 0.0

def animate(i, xs, ys):
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))

    xs.append(incrementor)
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
incrementor = incrementor + 1.0