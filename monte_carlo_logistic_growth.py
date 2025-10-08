import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

plt.style.use("bmh")

plt.rcParams["font.family"] = "Times New Roman"

def monte_carlo_logistic_growth(population_number=10, timestep=25):

    def logistic_growth_function(r, N, K): # r (growth rate), N (population at time t), K (carrying capacity)
        return r * N * (1 - (N/K))
    
    sim_data = []
    results = []
    for res in range(population_number):
        results.append([])

    for populations in range(population_number):

        r = random.uniform(0.01, 0.5)
        N = random.randrange(10, 1000)
        K = random.randrange(N, N*2)

        results[populations].append(N) # Initial Population

        sim_data.append({
            "Population": populations + 1,
            "r": f"{r:.3f}",
            "N0": N,
            "K": K
            })
        
        for sim in range(timestep):
            r_current = r + random.uniform(-0.02, 0.02) # Growth rate fluctuation
            N = N + logistic_growth_function(r_current, N, K)
            results[populations].append(N)

    for res in range(population_number):
        time_steps = range(len(results[res]))
        plt.scatter(0, results[res][0], color="blue", s=30)
        plt.plot(time_steps, results[res])
        # label=f"Population {res+1} (r={sim_data[res]['r']}, N0={sim_data[res]['N0']})" # Only applicable to small number of populations

    df = pd.DataFrame(sim_data)
    print(df.to_string(index=False))

    mean = np.mean(results, axis=0)
    std_dev = np.std(results, axis=0)
    median = np.median(results, axis=0)

    mean_val = np.mean(mean)
    std_val = np.mean(std_dev)
    median_val = np.mean(median)

    print(f"Median: {median_val:.3f}, Standard Deviation: {std_val:.3f}, Mean: {mean_val:.3f}")

    plt.plot(mean, color='red', linestyle="--", linewidth=3, label="Mean")
    plt.plot(median, color='purple', linestyle="--", linewidth=3, label="Median")
    plt.plot(std_dev, color='orange', linestyle="--", linewidth=3, label="Standard Deviation")
    plt.legend()
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Can be applied only if the population number is low and the individual labels implemented
    # plt.tight_layout() # Can be applied only if the population number is low and the individual labels implemented
    plt.title("Monte Carlo Simulation - Logistic Growth Function", fontsize=16)
    plt.xlabel("Time - t", fontsize=14)
    plt.ylabel("Population - P(t)", fontsize=14)
    # plt.yscale("log") # (If N varies widely across runs)
    plt.show()

    final_populations = [sim[-1] for sim in results]
    plt.hist(final_populations, bins=population_number, color="orange", alpha=0.7)
    plt.title("Distribution of Final Population Sizes")
    plt.xlabel("Population at The Final Timestep")
    plt.ylabel("Frequency")
    plt.show()

monte_carlo_logistic_growth()