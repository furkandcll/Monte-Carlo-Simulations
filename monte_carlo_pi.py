import random
import matplotlib.pyplot as plt

def monte_carlo_pi(attempts=1_000_000):
    sphere = 0
    for _ in range(attempts):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            sphere += 1
    result = (sphere/attempts) * 4
    print(result)

monte_carlo_pi()

#------------------------------------------------------------------------

def graph_monte_carlo_pi(attempts=10_000):
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    

    for i in range(attempts):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi = (len(x_inside)/attempts) * 4
    print("π has estimated as: ", pi)

    plt.scatter(x_inside, y_inside, color="red", s=1, label="Inside Circle")
    plt.scatter(x_outside, y_outside, color="blue", s=1, label="Outside Circle")
    plt.legend()
    plt.show()

graph_monte_carlo_pi()