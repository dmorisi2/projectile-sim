from config import MASS, GRAVITY, DT
from drag_models import compute_drag_force
import math

# dynamics.py
# ----------------------------------------------
# Computes accelerations and updates position and
# velocity using Newton's Laws

def update_motion(x_old, y_old, vx_old, vy_old):
    speed = math.sqrt((vx_old ** 2) + (vy_old ** 2))
    drag_force = compute_drag_force(speed)

    drag_force_x = 0
    drag_force_y = 0
    if (speed != 0):
        drag_force_x = -1 * drag_force * (vx_old / speed)
        drag_force_y = -1 * drag_force * (vy_old / speed)

    a_x = (drag_force_x / MASS)
    a_y = (drag_force_y / MASS) - GRAVITY


    vx_new = vx_old + (a_x * DT)
    vy_new = vy_old + (a_y * DT)
    x_new = x_old + (vx_new * DT)
    y_new = y_old + (vy_new * DT)

    return x_new, y_new, vx_new, vy_new
