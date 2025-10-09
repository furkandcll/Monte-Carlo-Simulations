import numpy as np
import matplotlib.pyplot as plt
import math

def diffusion(particle_number, timestep, stepsize, box_limit):

    particles = np.zeros((particle_number, 2))

    def motion(particles):

        plt.ion()

        for step in range(timestep):

            plt.clf()

            theta = np.random.uniform(0, 2 * math.pi, size=particle_number)

            particles[:, 0] += stepsize * np.cos(theta)
            particles[:, 1] += stepsize * np.sin(theta)

            std = np.std(particles, axis=0).mean()

            if step % 10 == 0:
                print(f"Step {step}: standard deviation = {std:.3f}")

            plt.scatter(particles[:, 0], particles[:, 1], color="royalblue", alpha=0.5)
            plt.xlim(- box_limit, box_limit)
            plt.ylim(-box_limit, box_limit)
            plt.pause(0.0001)
        
        plt.ioff()
        plt.show()

    motion(particles)

diffusion(500, 1000, 1, 100)