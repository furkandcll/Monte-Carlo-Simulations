import random
import math

def hypervolume_4d_sphere(n=1_000_000, epsilon=1e-6):
    
    count_inside = 0

    for _ in range(n):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        t = random.uniform(-1, 1)

        if x**2 + y**2 + z**2 + t**2 <= 1:
            count_inside += 1

    hypercube_volume = 16
    hypervolume = hypercube_volume * (count_inside / n)

    return hypervolume

result = hypervolume_4d_sphere()

print("The estimated hypervolume of the 4D unit sphere is: ", result)
print("The ratio between the estimated hypervolume of 4D unit sphere by Monte Carlo and deterministic 4D unit sphere hypervolume is: ", result / (math.pi**2 / 2))
print("The accuracy is: ", (result / (math.pi**2 / 2)) * 100)