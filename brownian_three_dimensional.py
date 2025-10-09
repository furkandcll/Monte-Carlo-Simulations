import numpy as np
import matplotlib.pyplot as plt
import math

def diffusion_3d(particle_number, timestep, stepsize, batch):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    particles = np.zeros((particle_number, 3))

    plt.ion()

    ax.set_autoscale_on(False)
    ax.set_title("3D Brownian Motion (Random Walk)")

    def motion(particles):

        for step in range(timestep):

            azimuthal = np.random.uniform(0, 2 * math.pi, size=particle_number)
            polar = np.random.uniform(- math.pi, math.pi, size=particle_number)

            particles[:, 0] += stepsize * np.cos(azimuthal)
            particles[:, 1] += stepsize * np.sin(azimuthal)
            particles[:, 2] += stepsize * np.sin(polar)

            std = np.std(particles, axis=0).mean()

            if step % 10 == 0:
                print(f"Step {step}: standard deviation = {std:.3f}")

            ax.cla()
            ax.scatter(particles[:, 0], particles[:, 1], particles[:, 2], color="royalblue", alpha=0.5)
            ax.set_xlim(-100, 100)
            ax.set_ylim(-100, 100)
            ax.set_zlim(-100, 100)
            ax.set_title(f"3D Brownian Motion - Step: {step}")
            plt.pause(0.01)

        plt.ioff()
        plt.show()

    motion(particles)

# diffusion_3d(500, 1000, 3, 10)

#---------------------------------------------------------------------------------------------------

def diffusion_3d_animation(particle_number, timestep, stepsize, batch):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    particles = np.zeros((particle_number, 3))

    plt.ion()

    ax.set_autoscale_on(False)

    def motion(particles):

        for step in range(timestep):

            azimuthal = np.random.uniform(0, 2 * math.pi, size=particle_number)
            polar = np.random.uniform(- math.pi, math.pi, size=particle_number)

            particles[:, 0] += stepsize * np.cos(azimuthal)
            particles[:, 1] += stepsize * np.sin(azimuthal)
            particles[:, 2] += stepsize * np.sin(polar)

            std = np.std(particles, axis=0).mean()

            if step % 10 == 0:
                print(f"Step {step}: standard deviation = {std:.3f}")

            if step % batch == 0:
                ax.cla()
                ax.scatter(particles[:, 0], particles[:, 1], particles[:, 2], color="royalblue", alpha=0.5)
                ax.set_xlim(-100, 100)
                ax.set_ylim(-100, 100)
                ax.set_zlim(-100, 100)
                ax.set_title(f"3D Brownian Motion - Step: {step}")
                plt.pause(0.01)
                # plt.savefig(f"{step}.png", dpi=300)

        plt.ioff()
        plt.show()

    motion(particles)

diffusion_3d_animation(500, 1000, 2, 10)