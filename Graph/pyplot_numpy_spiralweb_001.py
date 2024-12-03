# Spiral Web using Matplotlib and NumPy

import numpy as np
import matplotlib.pyplot as plt

def draw_spiral_web():
    # Parameters
    num_lines = 50  # Number of radial lines
    num_circles = 10  # Number of concentric circles
    max_radius = 10  # Maximum radius of the spiral web

    # Generate theta for radial lines (angle from 0 to 2*pi)
    theta = np.linspace(0, 2 * np.pi, num_lines, endpoint=False)

    # Generate radii for concentric circles
    radii = np.linspace(0, max_radius, num_circles)

    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    ax.set_facecolor('black')  # Set background color to black
    ax.set_xticks([])  # Remove angular ticks
    ax.set_yticks([])  # Remove radial ticks

    # Draw radial lines
    for t in theta:
        ax.plot([t, t], [0, max_radius], color='cyan', linewidth=0.7)

    # Draw concentric circles
    for r in radii:
        ax.plot(np.linspace(0, 2 * np.pi, 100), [r] * 100, color='cyan', linewidth=0.7)

    # Add a spiral
    spiral_theta = np.linspace(0, 4 * np.pi, 500)  # 2 full rotations
    spiral_r = np.linspace(0, max_radius, 500)
    ax.plot(spiral_theta, spiral_r, color='yellow', linewidth=1)

    # Set aspect ratio and display the plot
    ax.set_ylim(0, max_radius)
    plt.show()

# Call the function to draw the spiral web
if __name__ == "__main__":
    draw_spiral_web()
