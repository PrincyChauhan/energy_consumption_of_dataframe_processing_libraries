# # from pyJoules.energy_meter import measure_energy
# # from pyJoules.handler.csv_handler import CSVHandler
# # import time
# # import numpy as np
# # import pandas as pd  # Import pandas for JSON and HDF5 operations
# # import chardet

# # # Initialize CSVHandler for energy measurement logging
# # csv_handler = CSVHandler('numpy_drug.csv')

# # def sleep():
# #     time.sleep(30)

# # def detect_encoding(path):
# #     with open(path, 'rb') as f:
# #         result = chardet.detect(f.read())
# #     return result['encoding']

# # @measure_energy(handler=csv_handler)
# # def load_csv_with_numpy(path):
# #     try:
# #         encoding = detect_encoding(path)  # Detect encoding
# #         data = np.genfromtxt(path, delimiter=',', skip_header=1, filling_values=np.nan, encoding=encoding)
# #         print(f"Loaded data with shape: {data.shape}")
# #         return data
# #     except Exception as e:
# #         print(f"Error loading file: {e}")
# #         return None

# # @measure_energy(handler=csv_handler)
# # def save_csv_with_numpy(data, path):
# #     try:
# #         np.savetxt(path, data, delimiter=',', fmt='%s')  # Save as CSV using NumPy
# #         print(f"Saved data to {path}")
# #     except Exception as e:
# #         print(f"Error saving file: {e}")

# # @measure_energy(handler=csv_handler)
# # def replace_nan(data, value=0):
# #     # Replace NaN values with the specified value
# #     return np.nan_to_num(data, nan=value)

# # # @measure_energy(handler=csv_handler)
# # # def calculate_sum(data):
# # #     return np.nansum(data)

# # # @measure_energy(handler=csv_handler)
# # # def calculate_mean(data):
# # #     return np.nanmean(data)

# # # @measure_energy(handler=csv_handler)
# # # def calculate_min(data):
# # #     return np.nanmin(data)

# # # @measure_energy(handler=csv_handler)
# # # def calculate_max(data):
# # #     return np.nanmax(data)

# # def load_json(path):
# #     try:
# #         return pd.read_json(path)
# #     except Exception as e:
# #         print(f"Error loading JSON file: {e}")
# #         return None

# # def save_json(df, path):
# #     try:
# #         df.to_json(path, orient='records')
# #         print(f"Saved JSON to {path}")
# #     except Exception as e:
# #         print(f"Error saving JSON file: {e}")

# # def load_hdf(path):
# #     try:
# #         return pd.read_hdf(path, key='_data')
# #     except Exception as e:
# #         print(f"Error loading HDF5 file: {e}")
# #         return None

# # def save_hdf(df, path, key='_data'):
# #     try:
# #         df.to_hdf(path, key=key)
# #         print(f"Saved HDF5 to {path}")
# #     except Exception as e:
# #         print(f"Error saving HDF5 file: {e}")

# # print("Starting NumPy Process...")
# # for i in range(10):
# #     # Input-output functions
# #     data = load_csv_with_numpy(path='../Datasets/drugs.csv')
# #     if data is not None:
# #         sleep()
# #         save_csv_with_numpy(data, f'df_numpy_drugs_{i}.csv')
# #         sleep()

# #         # Load and save JSON
# #         df = load_json('../Datasets/drugs.json')
# #         if df is not None:
# #             sleep()
# #             save_json(df, f'df_numpy_drugs_{i}.json')
# #             sleep()

# #         # Load and save HDF5
# #         df = load_hdf('../Datasets/drugs.h5')
# #         if df is not None:
# #             sleep()
# #             save_hdf(df, f'df_numpy_drugs_{i}.h5', key='_data')
# #             sleep()
    
# #         # Handling missing data
# #         # data = replace_nan(data)
# #         # sleep()

# #         # # Statistical operations
# #         # print(f"Sum: {calculate_sum(data)}")
# #         # sleep()
# #         # print(f"Mean: {calculate_mean(data)}")
# #         # sleep()
# #         # print(f"Min: {calculate_min(data)}")
# #         # sleep()
# #         # print(f"Max: {calculate_max(data)}")
# #         # sleep()

# #         print(f"Finished {i+1} iterations.")

# # csv_handler.save_data()
# # print("NumPy Process ended...")

# import numpy as np
# import json
# import h5py
# import time
# from pyJoules.energy_meter import measure_energy
# from pyJoules.handler.csv_handler import CSVHandler

# csv_handler = CSVHandler('numpy_drug.csv')

# def sleep():
#     time.sleep(30)

# # I/O functions - READ
# @measure_energy(handler=csv_handler)
# def load_csv(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         return np.genfromtxt(f, delimiter=',', skip_header=1)

# @measure_energy(handler=csv_handler)
# def load_json(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         return np.array(data)  # Convert the JSON data to a NumPy array

# @measure_energy(handler=csv_handler)
# def load_hdf(path):
#     with h5py.File(path, 'r') as f:
#         return np.array(f['dataset'])  # Replace 'dataset' with the actual dataset name

# # I/O functions - WRITE
# @measure_energy(handler=csv_handler)
# def save_csv(arr, path):
#     np.savetxt(path, arr, delimiter=',')

# @measure_energy(handler=csv_handler)
# def save_json(arr, path):
#     with open(path, 'w', encoding='utf-8') as f:
#         json.dump(arr.tolist(), f)  # Convert NumPy array to list before saving

# @measure_energy(handler=csv_handler)
# def save_hdf(arr, path, key):
#     with h5py.File(path, 'w') as f:
#         f.create_dataset(key, data=arr)

# ###------------------------------------------###

# # Handling missing data 
# @measure_energy(handler=csv_handler)
# def isna(arr):
#     return np.isnan(arr)

# @measure_energy(handler=csv_handler)
# def dropna(arr):
#     return arr[~np.isnan(arr)]

# @measure_energy(handler=csv_handler)
# def fillna(arr, val):
#     arr[np.isnan(arr)] = val
#     return arr

# @measure_energy(handler=csv_handler)
# def replace(arr, src, dest):
#     return np.where(arr == src, dest, arr)

# ###------------------------------------------###

# # Table operations
# # drop column
# # groupby
# # merge 
# # transpose
# # sort
# # concat
# @measure_energy(handler=csv_handler)
# def drop(arr, idx):
#     return np.delete(arr, idx, axis=1)

# @measure_energy(handler=csv_handler)
# def groupby(arr, col_idx):
#     # Assuming groupby works by sorting the array by the column index
#     return arr[arr[:, col_idx].argsort()]

# @measure_energy(handler=csv_handler)
# def merge(arr1, arr2, axis=0):
#     return np.concatenate((arr1, arr2), axis=axis)

# @measure_energy(handler=csv_handler)
# def sort(arr, col_idx):
#     return arr[arr[:, col_idx].argsort()]

# @measure_energy(handler=csv_handler)
# def concat_dataframes(arr1, arr2):
#     return np.concatenate((arr1, arr2), axis=0)

# ###--------------------------------------------###
# # Statistical Operations
# # min, max, mean, count, unique, correlation

# # count 
# @measure_energy(handler=csv_handler)
# def count(arr):
#     return arr.shape[0]

# # sum
# @measure_energy(handler=csv_handler)
# def sum(arr):
#     return np.nansum(arr)

# # mean
# @measure_energy(handler=csv_handler)
# def mean(arr):
#     return np.nanmean(arr)

# # min
# @measure_energy(handler=csv_handler)
# def min(arr):
#     return np.nanmin(arr)

# # max
# @measure_energy(handler=csv_handler)
# def max(arr):
#     return np.nanmax(arr)

# # unique
# @measure_energy(handler=csv_handler)
# def unique(arr):
#     return np.unique(arr)

# ###------------------------------------------###

# print("Starting NumPy Drug Process...")
# for i in range(10):
#     # Input output functions 
#     arr_csv = load_csv(path='../Datasets/drugs.csv')
#     sleep()
#     arr_json = load_json(path='../Datasets/drugs.json')
#     sleep()
#     arr_hdf = load_hdf(path='../Datasets/drugs.h5')
#     sleep()

#     save_csv(arr_csv, f'df_drug_numpy{i}.csv')
#     sleep()
#     save_json(arr_json, f'df_drug_numpy{i}.json')
#     sleep()
#     save_hdf(arr_hdf, f'df_drug_numpy{i}.h5', key='dataset')
#     sleep()

#     # --------------------------------------------------

#     # Handling missing data
#     arr = load_csv('../Datasets/drugs.csv')
#     sleep()
#     isna(arr)
#     sleep()
#     arr = dropna(arr)
#     sleep()
#     arr = fillna(arr, val=0)
#     sleep()
#     arr = replace(arr, src=0, dest=1)
#     sleep()

#     # --------------------------------------------------
#     # Table operations
#     arr = load_csv('../Datasets/drugs.csv')
#     arr_samp = load_csv('../Datasets/drugs.csv')
#     sleep()
#     arr = drop(arr, idx=[1])  # Drop column at index 1
#     sleep()
#     arr = groupby(arr, col_idx=2)  # Group by the third column (index 2)
#     sleep()

#     arr = concat_dataframes(arr, arr_samp)
#     sleep()

#     arr = sort(arr, col_idx=2)  # Sort by the third column (index 2)
#     sleep()
#     arr = merge(arr, arr_samp)
#     sleep()

#     # ------------------------------------------
#     # Statistical operations
#     arr = load_csv('../Datasets/drugs.csv')
#     sleep()
#     count(arr)
#     sleep()
#     sum(arr)
#     sleep()
#     mean(arr)
#     sleep()
#     min(arr)
#     sleep()
#     max(arr)
#     sleep()
#     unique(arr)
#     sleep()

#     print(f"Finished {i+1} iterations.")

# csv_handler.save_data()
# print("Process ended...")


from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import time
import numpy as np
import pandas as pd  # Import pandas for JSON and HDF5 operations

# Initialize CSVHandler for energy measurement logging
csv_handler = CSVHandler('drug_numpy_1.24.4.csv')

def sleep():
    time.sleep(30)

@measure_energy(handler=csv_handler)
def load_csv(path):
    try:
        # Use pandas to load the CSV and handle potential inconsistent rows
        df = pd.read_csv(path, delimiter=',', on_bad_lines='skip')
        return df.values  # Convert to a NumPy array
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return np.array([])

@measure_energy(handler=csv_handler)
def save_csv(array, path):
    try:
        # Open the file with utf-8 encoding to handle special characters
        with open(path, 'w', encoding='utf-8') as f:
            # Save the array as a CSV with proper encoding
            np.savetxt(f, array, delimiter=',', fmt='%s')
    except Exception as e:
        print(f"Error saving CSV: {e}")
        
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

###------------------------------------------###

print("Starting drug reviews dataset process...")

for i in range(10):
    # Input-output functions
    array = load_csv(path='../datasets/drugs.csv')
    sleep()
    save_csv(array, f'df_numpy_drug_reviews_{i}.csv')
    sleep()

    # Load and save JSON
    df = load_json('../datasets/drugs.json')
    sleep()
    save_json(df, f'df_numpy_drug_reviews_{i}.json')
    sleep()

    # Load and save HDF5
    df = load_hdf('../datasets/drugs.h5')
    sleep()
    save_hdf(df, f'df_numpy_drug_reviews_{i}.h5', key='drug_reviews_data')
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
print("Drug reviews dataset process ended...")
