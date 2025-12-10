# data_logger.py
# ----------------------------------------------
# Saves simulation data to a CSV file using Pandas.

import pandas as pd
import os

def save_simulation_data(run_name, times, x_positions, y_positions, vx_values, vy_values):
    run_path = os.path.join("runs", run_name)
    os.makedirs(run_path, exist_ok=True)

    data = pd.DataFrame({
        "time":times,
        "x_position": x_positions,
        'y_position': y_positions,
        "x_velocity": vx_values,
        "y_velocity": vy_values
    })

    file_path = os.path.join(run_path, "trajectory.csv")
    data.to_csv(file_path, index=False)

    print(f"Simulation data saved to: {file_path}")