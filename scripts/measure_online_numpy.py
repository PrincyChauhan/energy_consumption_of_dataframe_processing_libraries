from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import time
import numpy as np
import pandas as pd  # Import pandas for JSON and HDF5 operations

# Initialize CSVHandler for energy measurement logging
csv_handler = CSVHandler('onlineretail_numpy_1.24.4.csv')

def sleep():
    time.sleep(30)

@measure_energy(handler=csv_handler)
def load_csv(path):
    try:
        # Use pandas to load the CSV and handle potential inconsistent rows more flexibly
        df = pd.read_csv(path, delimiter=',', on_bad_lines='skip')
        return df.values  # Convert to a NumPy array
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return np.array([])

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

###------------------------------------------###

# Handling missing data 
@measure_energy(handler=csv_handler)
def replace_nan(array, value=0):
    # Loop through each column and check if it's numeric
    for i in range(array.shape[1]):
        try:
            # Convert the column to float (if possible) and apply np.isnan()
            array[:, i] = np.where(np.isnan(array[:, i].astype(float)), value, array[:, i])
        except ValueError:
            # If conversion to float fails, skip the column
            continue
    return array

###------------------------------------------###

# Statistical Operations using NumPy

@measure_energy(handler=csv_handler)
def calculate_sum(array):
    # Ensure the array is 2D and handle numeric data
    numeric_data = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_data.append(column)
        except ValueError:
            continue

    if not numeric_data:
        return "No numeric data"

    numeric_data = np.array(numeric_data).T
    return np.sum(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_mean(array):
    numeric_data = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_data.append(column)
        except ValueError:
            continue

    if not numeric_data:
        return "No numeric data"

    numeric_data = np.array(numeric_data).T
    return np.mean(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_min(array):
    numeric_data = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_data.append(column)
        except ValueError:
            continue

    if not numeric_data:
        return "No numeric data"

    numeric_data = np.array(numeric_data).T
    return np.min(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_max(array):
    numeric_data = []
    for i in range(array.shape[1]):
        try:
            column = array[:, i].astype(float)
            numeric_data.append(column)
        except ValueError:
            continue

    if not numeric_data:
        return "No numeric data"

    numeric_data = np.array(numeric_data).T
    return np.max(numeric_data)

print("Starting Online Retail Process...")
for i in range(10):
    # Input-output functions
    array = load_csv(path='../datasets/onlineretail.csv')
    sleep()
    save_csv(array, f'df_numpy_onlineretail_{i}.csv')
    sleep()

    # Load and save JSON
    df = load_json('../datasets/onlineretail.json')
    sleep()
    save_json(df, f'df_numpy_onlineretail_{i}.json')
    sleep()

    # Load and save HDF5
    df = load_hdf('../datasets/onlineretail.h5')
    sleep()
    save_hdf(df, f'df_numpy_onlineretail_{i}.h5', key='onlineretail_data')
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
print("Online Retail Process ended...")
