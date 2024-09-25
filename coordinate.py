import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

def rotation_matrix(theta, phi):
    """
    Calculate the rotation matrix for given theta and phi angles.
    theta: rotation around y-axis
    phi: rotation around z-axis
    """
    Ry = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    
    Rz = np.array([
        [np.cos(phi), -np.sin(phi), 0],
        [np.sin(phi), np.cos(phi), 0],
        [0, 0, 1]
    ])
    
    return Rz @ Ry

def update(val):
    theta = theta_slider.val
    phi = phi_slider.val
    
    R = rotation_matrix(theta, phi)
    
    # Update rotated axes
    for i in range(3):
        rotated_axes[i].set_data([0, R[0, i]], [0, R[1, i]])
        rotated_axes[i].set_3d_properties([0, R[2, i]])
    
    # Update matrix text
    matrix_text.set_text(f"Rotation Matrix:\n{R}")
    
    # Update formula text
    formula_text.set_text(
        f"R = Rz(φ) * Ry(θ) =\n"
        f"[[cos(φ)cos(θ), -sin(φ), cos(φ)sin(θ)],\n"
        f"[sin(φ)cos(θ), cos(φ), sin(φ)sin(θ)],\n"
        f"[-sin(θ), 0, cos(θ)]]\n\n"
        f"θ = {theta:.2f}, φ = {phi:.2f}"
    )
    
    fig.canvas.draw_idle()

# Create the figure and 3D axis
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(121, projection='3d')

# Plot original coordinate system
ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

# Plot rotated coordinate system
rotated_axes = [
    ax.plot([0, 1], [0, 0], [0, 0], 'r--')[0],
    ax.plot([0, 0], [0, 1], [0, 0], 'g--')[0],
    ax.plot([0, 0], [0, 0], [0, 1], 'b--')[0]
]

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Rotation Visualization')

# Add sliders for theta and phi
ax_theta = plt.axes([0.2, 0.02, 0.6, 0.03])
ax_phi = plt.axes([0.2, 0.06, 0.6, 0.03])
theta_slider = Slider(ax_theta, 'θ', 0, 2*np.pi, valinit=0)
phi_slider = Slider(ax_phi, 'φ', 0, 2*np.pi, valinit=0)

# Add text area for matrix display
ax_text = fig.add_subplot(122)
ax_text.axis('off')
matrix_text = ax_text.text(0.1, 0.7, "", fontsize=10)
formula_text = ax_text.text(0.1, 0.3, "", fontsize=10)

# Connect the sliders to the update function
theta_slider.on_changed(update)
phi_slider.on_changed(update)

# Initial update
update(None)

plt.tight_layout()
plt.show()