from config import AIR_DENSITY, DRAG_COEFFICIENT, AREA

# drag_models.py
# ----------------------------------------------
# Computation of the drag force using the current
# speed.
def compute_drag_force(v):
    return 0.5 * AIR_DENSITY * DRAG_COEFFICIENT * AREA * (v ** 2)
