import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# --- ASTRONOMICAL PARAMETERS ---
earth_orbit_radius = 1.0       # 1 AU
moon_orbit_radius = 0.0025     # Moon's orbital radius (AU)
wobble_scale = 15              # Scale factor for visibility
moon_frequency = 13            # Integer cycles per Earth orbit (close to actual 13.37)

# --- TIME ARRAY ---
num_points = 1000              # High resolution for smooth curve
t = np.linspace(0, 2*np.pi, num_points)

# --- SET UP FIGURE ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(alpha=0.2)
plt.title("Moon's Wavy Path Around the Sun (1 Year)", fontsize=14)
plt.xlabel("Distance from Sun (AU)")
plt.ylabel("Distance from Sun (AU)")

# --- CREATE STATIC PLOT ELEMENTS ---
# Sun
sun = plt.Circle((0, 0), 0.1, color='yellow', zorder=10)
ax.add_patch(sun)

# Earth's orbit (dashed circle)
earth_orbit = plt.Circle((0, 0), earth_orbit_radius, 
                        color='blue', fill=False, 
                        linestyle='--', alpha=0.3)
ax.add_patch(earth_orbit)

# Calculate all positions at once
earth_x = np.cos(t) * earth_orbit_radius
earth_y = np.sin(t) * earth_orbit_radius
moon_x = earth_x + np.cos(t * moon_frequency) * moon_orbit_radius * wobble_scale
moon_y = earth_y + np.sin(t * moon_frequency) * moon_orbit_radius * wobble_scale

# Plot Earth's starting position
earth_start = ax.plot(earth_x[0], earth_y[0], 'bo', 
                     markersize=10, label="Earth start")

# Plot Moon's starting position
moon_start = ax.plot(moon_x[0], moon_y[0], 'ro', 
                    markersize=5, label="Moon start")

# Plot Moon's complete path
moon_path = ax.plot(moon_x, moon_y, 'r-', 
                   alpha=0.7, linewidth=1.5, 
                   label="Moon's path (×15 scale)")

# Add legend
ax.legend(loc='upper right')

plt.show()

# To save the plot (uncomment):
# plt.savefig('moon_orbit_static.png', dpi=200, bbox_inches='tight')
