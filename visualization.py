# visualization.py
# ----------------------------------------------
# Plots the trajectory of the projectile.

import matplotlib.pyplot as plt
def plot_trajectory(x_positions, y_positions):
    plt.figure()
    plt.plot(x_positions, y_positions)
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.title("Projectile Motion Trajectory")
    plt.grid(True)
    plt.show()
