import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from matplotlib import style

plt.style.use('ggplot')

fig = plt.figure()
fig.suptitle('Grafik Ketinggian', fontsize=8, fontweight='bold')
fig.set_size_inches(6, 4)
ax1 = fig.add_subplot(1, 1, 1)

def generate_random_data(timestamp):
    with open('data.txt', 'a') as file:
        for i in range(1):
            ketinggian = random.randint(0, 100)
            pitch = random.randint(0, 20)
            file.write(f"{ketinggian}, {timestamp}, {pitch}\n")
        print(ketinggian)

def animate(i):
    graph_data = open('data.txt', 'r').readlines()
    lines = graph_data[1:]
    xs = []
    ys = []
    zs = []
    for line in lines:
        if len(line) > 1:
            y, x, z = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    # print (xs + ys + zs)
    ax1.clear()
    ax1.plot(xs, ys, zs)
    #ax1.plot(xs, zs)
    ax1.set_ylabel("Ketinggian")
    ax1.set_xlabel("TimeStamp (s)")
    plt.savefig("Hasil_Update_PNG.png")

open('data.txt', 'w').close()

timestamp = -1
ani = animation.FuncAnimation(fig, animate, interval=1000)

while True:
    generate_random_data(timestamp)
    timestamp += 1
    plt.pause(1)
