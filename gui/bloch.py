import numpy as np
import matplotlib.pyplot as plt
from cmath import phase

def plot_bloch_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Bloch Sphere")

    # Wireframe of the Bloch sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_wireframe(x, y, z, color='m', alpha=0.1)

    # Red=x-axis, Green=y-axis, Blue=z-axis
    ax.quiver(0, 0, 0, 1.5, 0, 0, color='r', arrow_length_ratio=0.1)  # Positive x-axis
    ax.quiver(0, 0, 0, -1.5, 0, 0, color='r', arrow_length_ratio=0.1)  # Negative x-axis
    ax.quiver(0, 0, 0, 0, 1.5, 0, color='g', arrow_length_ratio=0.1)  # Positive y-axis
    ax.quiver(0, 0, 0, 0, -1.5, 0, color='g', arrow_length_ratio=0.1)  # Negative y-axis
    ax.quiver(0, 0, 0, 0, 0, 1.5, color='b', arrow_length_ratio=0.1)  # Positive z-axis
    ax.quiver(0, 0, 0, 0, 0, -1.5, color='b', arrow_length_ratio=0.1)  # Negative z-axis

    # Adding Labels
    ax.text(1.1, 0, 0, r'X|+⟩', color='r')
    ax.text(-1.2, 0, 0, r'-X|-⟩', color='r')
    ax.text(0, 1.1, 0, r'Y|i⟩', color='g')
    ax.text(0, -1.2, 0, r'-Y|-i⟩', color='g')
    ax.text(0, 0, 1.1, r'Z|0⟩', color='b')
    ax.text(0, 0, -1.2, r'-Z|1⟩', color='b')


    # Limits and aspect ratio
    ax.set_box_aspect([2, 2, 2])
    ax.set_xlim([-1.3, 1.3])
    ax.set_ylim([-1.3, 1.3])
    ax.set_zlim([-1.3, 1.3])

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.axis('off')

    return fig, ax

def update_bloch_sphere(ax, state_vector, quiver_ref=None, scatter_ref=None, num_frames=30):
    theta = 2 * np.arccos(abs(state_vector[0]))
    phi = phase(state_vector[1])-phase(state_vector[0])
    print('theta',theta)
    print('phi',phi)
    # Convert spherical coordinates to Cartesian coordinates
    new_x = np.sin(theta) * np.cos(phi)
    new_y = np.sin(theta) * np.sin(phi)
    new_z = np.cos(theta)

    if quiver_ref:
        # Get the current arrow position
        old_x = quiver_ref._segments3d[0][1][0]
        old_y = quiver_ref._segments3d[0][1][1]
        old_z = quiver_ref._segments3d[0][1][2]
    else:
        old_x, old_y, old_z = 0, 0, 0

    for t in np.linspace(0, 1, num_frames):
        x = old_x * (1 - t) + new_x * t
        y = old_y * (1 - t) + new_y * t
        z = old_z * (1 - t) + new_z * t

        # Remove previous quiver and scatter
        if quiver_ref:
            quiver_ref.remove()
        if scatter_ref:
            scatter_ref.remove()

        quiver_ref = ax.quiver(0, 0, 0, x, y, z, color='w', arrow_length_ratio=0.3)  # Change color to white
        scatter_ref = ax.scatter([x], [y], [z], color='w', s=100)  # Change color to white
        plt.draw()
        plt.pause(0.05)

    return quiver_ref, scatter_ref
