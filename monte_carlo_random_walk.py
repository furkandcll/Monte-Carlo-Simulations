import random
import matplotlib.pyplot as plt

def random_walk(sample=1_000):

    x = [0]
    y = [0]

    for _ in range(sample):
        x.append(x[-1] + random.randint(-1, 1))
        y.append(y[-1] + random.randint(-1, 1))
    

    plt.plot(x, y, linestyle="--", color='blue', lw=0.5)
    plt.scatter(x[0], y[0], color='green', label='Start', s=50)
    plt.scatter(x[-1], y[-1], color='red', label='End', s=50)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("2D Random Walk")
    plt.legend()
    plt.grid(True)
    plt.show()

random_walk()

# #----------------------------------------------------------------------------------------------

def random_walk_three_dimensional(sample=1_000):
    
    x = [0]
    y = [0]
    z = [0]

    for _ in range(sample):
        x.append(x[-1] + random.randint(-1, 1))
        y.append(y[-1] + random.randint(-1, 1))
        z.append(z[-1] + random.randint(-1, 1))
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='blue', lw=0.5)
    ax.scatter(x[0], y[0], z[0], color='green', label='Start', s=50)
    ax.scatter(x[-1], y[-1], z[-1], color='red', label='End', s=50)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Random Walk")
    ax.legend()
    plt.show()

random_walk_three_dimensional()

# #----------------------------------------------------------------------------------------------

def random_walk_three_dimensional_animation(sample=1_000, batch=5):

    plt.ion()

    x = [0]
    y = [0]
    z = [0]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    for i in range(sample):

        x.append(x[-1] + random.randint(-1, 1))
        y.append(y[-1] + random.randint(-1, 1))
        z.append(z[-1] + random.randint(-1, 1))
    
        if i % batch == 0 or i == sample - 1:
            ax.cla()
            ax.plot(x, y, z, color='blue', lw=0.5)
            ax.scatter(x[0], y[0], z[0], color='green', label='Start', s=50)
            ax.scatter(x[-1], y[-1], z[-1], color='red', label='End', s=50)
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")
            ax.set_title(f"3D Random Walk (step {i})")
            ax.legend()
            plt.pause(0.001)
            # plt.savefig(f"{i}.png", dpi=300)

    plt.ioff()
    plt.show()

random_walk_three_dimensional_animation()