from dynamics import update_motion
from config import DT

# simulation.py
# ----------------------------------------------
# Runs the full simulation loop.
def simulate_projectile(x0, y0, vx0, vy0):
    x = x0
    y = y0
    vx = vx0
    vy = vy0
    t = 0.0

    times = []
    x_positions = []
    y_positions = []
    vx_values = []
    vy_values = []

    while y >= 0:
        times.append(t)
        x_positions.append(x)
        y_positions.append(y)
        vx_values.append(vx)
        vy_values.append(vy)

        x, y, vx, vy = update_motion(x, y, vx, vy)
        t += DT

    return times, x_positions, y_positions, vx_values, vy_values