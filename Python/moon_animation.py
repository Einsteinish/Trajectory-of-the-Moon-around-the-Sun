import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# --- ASTRONOMICAL PARAMETERS ---
earth_orbit_radius = 1.0       # 1 AU
moon_orbit_radius = 0.0025     # Moon's orbital radius (AU)
wobble_scale = 15              # Scale factor for visibility
moon_frequency = 13            # Integer cycles per Earth orbit for a closed loop (close to the actual 13.36875 synodic months)

# --- TIME ARRAY ---
num_frames = 200               # Number of animation frames
t = np.linspace(0, 2*np.pi, num_frames)

# --- SET UP FIGURE ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(alpha=0.2)
plt.title("Moon's Wavy Path Around the Sun", fontsize=14)
plt.xlabel("Distance from Sun (AU)")
plt.ylabel("Distance from Sun (AU)")

# --- CREATE ARTISTS ---
sun = plt.Circle((0, 0), 0.1, color='yellow', zorder=10)
earth_orbit = plt.Circle((0, 0), earth_orbit_radius, color='blue', 
                        fill=False, linestyle='--', alpha=0.3)
earth_dot, = ax.plot([], [], 'bo', markersize=10, label="Earth")
moon_dot, = ax.plot([], [], 'ro', markersize=5, label="Moon")
path_line, = ax.plot([], [], 'r-', alpha=0.5, linewidth=1, label="Moon's path")

# Add to axes
ax.add_patch(sun)
ax.add_patch(earth_orbit)
ax.legend(loc='upper right')

# --- ANIMATION FUNCTION ---
def update(frame):
    # Calculate positions
    earth_x = np.cos(t[frame]) * earth_orbit_radius
    earth_y = np.sin(t[frame]) * earth_orbit_radius
    
    moon_x = earth_x + np.cos(t[frame] * moon_frequency) * moon_orbit_radius * wobble_scale
    moon_y = earth_y + np.sin(t[frame] * moon_frequency) * moon_orbit_radius * wobble_scale
    
    # Update Earth and Moon positions
    earth_dot.set_data(earth_x, earth_y)
    moon_dot.set_data(moon_x, moon_y)
    
    # Update Moon's path (show full history)
    path_line.set_data(
        earth_orbit_radius * np.cos(t[:frame+1]) + 
        moon_orbit_radius * wobble_scale * np.cos(t[:frame+1] * moon_frequency),
        earth_orbit_radius * np.sin(t[:frame+1]) + 
        moon_orbit_radius * wobble_scale * np.sin(t[:frame+1] * moon_frequency)
    )
    
    return earth_dot, moon_dot, path_line

# --- CREATE ANIMATION ---
ani = FuncAnimation(
    fig, update, frames=num_frames, 
    interval=50, blit=True, repeat=True
)

plt.show()

# To save the animation (uncomment):
ani.save('moon_orbit.mp4', writer='ffmpeg', fps=30, dpi=200)
