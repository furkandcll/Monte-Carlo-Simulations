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

def graph_monte_carlo_pi(attempts=100_000, batch=1000):
    x_inside, y_inside, x_outside, y_outside = [], [], [], []

    plt.ion()

    for i in range(attempts):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

        pi_estimation = (len(x_inside) / (i+1)) * 4

        if i % batch == 0:
            plt.clf()
            plt.scatter(x_inside, y_inside, color="red", s=1, label="Inside Circle")
            plt.scatter(x_outside, y_outside, color="blue", s=1, label="Outside Circle")
            plt.legend(loc="lower center")
            plt.title("Monte Carlo Simulation - Estimation of π", fontsize=20, fontname="Times New Roman")

            plt.text(0.5, -0.3,
                    f"Inside: {len(x_inside):,} | Outside: {len(x_outside):,}",
                    fontsize=16, ha="right", va="bottom",
                    fontname="Times New Roman")

            plt.text(1, -0.3,
                    f"π ≈ {pi_estimation:.6f}",
                    fontsize=16, ha="right", va="bottom",
                    fontname="Times New Roman")

            plt.subplots_adjust(bottom=0.25)

            plt.pause(0.001)
            #  plt.savefig(f"{i}.png", dpi=300)

    pi = (len(x_inside) / attempts) * 4
    print("π has been estimated as:", pi)

    plt.ioff()
    plt.show()

graph_monte_carlo_pi()
