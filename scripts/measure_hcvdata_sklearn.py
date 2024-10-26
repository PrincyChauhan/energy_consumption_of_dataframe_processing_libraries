from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import time
import numpy as np
import pandas as pd

# Initialize CSVHandler for energy measurement logging
csv_handler = CSVHandler('hcv_numpy.csv')

def sleep():
    time.sleep(30)

@measure_energy(handler=csv_handler)
def load_csv(path):
    # Load data using pandas to handle mixed data types and headers more gracefully
    try:
        df = pd.read_csv(path)  # Automatically handles headers and mixed data types
        return df.values  # Convert DataFrame to NumPy array
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return np.array([])  # Return an empty array if loading fails

@measure_energy(handler=csv_handler)
def save_csv(array, path):
    # Convert the array to a string format to ensure all data types are handled correctly
    np.savetxt(path, array, delimiter=',', fmt='%s')

@measure_energy(handler=csv_handler)
def load_json(path):
    return pd.read_json(path)

@measure_energy(handler=csv_handler)
def save_json(df, path):
    return df.to_json(path, orient='records')

@measure_energy(handler=csv_handler)
def load_hdf(path):
    return pd.read_hdf(path)

@measure_energy(handler=csv_handler)
def save_hdf(df, path, key):
    return df.to_hdf(path, key=key, mode='w')

# Handling missing data 
@measure_energy(handler=csv_handler)
def replace_nan(array, value=0):
    for i in range(array.shape[1]):
        try:
            array[:, i] = np.where(np.isnan(array[:, i].astype(float)), value, array[:, i])
        except ValueError:
            continue
    return array

# Statistical Operations using NumPy
@measure_energy(handler=csv_handler)
def calculate_sum(array):
    if len(array.shape) != 2:
        print(f"Error: Expected 2D array, but got {array.shape}.")
        return "Invalid array shape"

    numeric_columns = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_columns.append(column)
        except ValueError:
            continue

    if not numeric_columns:
        return "No numeric data"

    numeric_data = np.array(numeric_columns).T
    return np.sum(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_mean(array):
    if len(array.shape) != 2:
        print(f"Error: Expected 2D array, but got {array.shape}.")
        return "Invalid array shape"

    numeric_columns = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_columns.append(column)
        except ValueError:
            continue

    if not numeric_columns:
        return "No numeric data"

    numeric_data = np.array(numeric_columns).T
    return np.mean(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_min(array):
    if len(array.shape) != 2:
        print(f"Error: Expected 2D array, but got {array.shape}.")
        return "Invalid array shape"

    numeric_columns = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_columns.append(column)
        except ValueError:
            continue

    if not numeric_columns:
        return "No numeric data"

    numeric_data = np.array(numeric_columns).T
    return np.min(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_max(array):
    if len(array.shape) != 2:
        print(f"Error: Expected 2D array, but got {array.shape}.")
        return "Invalid array shape"

    numeric_columns = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_columns.append(column)
        except ValueError:
            continue

    if not numeric_columns:
        return "No numeric data"

    numeric_data = np.array(numeric_columns).T
    return np.max(numeric_data)

# Main Execution for HCV Dataset
print("Starting HCV Process...")
for i in range(10):
    # Input-output functions
    array = load_csv(path='../datasets/hcvdata.csv')
    print(f"Loaded array shape: {array.shape}")
    sleep()
    save_csv(array, f'df_hcv_{i}.csv')
    sleep()

    # Load and save JSON
    df = load_json('../datasets/hcvdata.json')
    sleep()
    save_json(df, f'df_hcv_{i}.json')
    sleep()

    # Load and save HDF5
    df = load_hdf('../datasets/hcvdata.h5')
    sleep()
    save_hdf(df, f'df_hcv_{i}.h5', key='hcv_data')
    sleep()
    
    # Handling missing data
    array = replace_nan(array)
    sleep()

    # Statistical operations
    print(f"Sum: {calculate_sum(array)}")
    sleep()
    print(f"Mean: {calculate_mean(array)}")
    sleep()
    print(f"Min: {calculate_min(array)}")
    sleep()
    print(f"Max: {calculate_max(array)}")
    sleep()

    print(f"Finished {i+1} iterations.")

csv_handler.save_data()
print("HCV Process ended...")
