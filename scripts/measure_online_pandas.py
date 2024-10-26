from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import time
import pandas as pd

# CSV handler to save energy measurements
csv_handler = CSVHandler('onlineretail.csv')

# Sleep function for intervals between operations
def sleep():
    time.sleep(30)
    
# I/O functions - READ
@measure_energy(handler=csv_handler)
def load_csv(path):
    return pd.read_csv(path)

@measure_energy(handler=csv_handler)
def load_hdf(path):
    return pd.read_hdf(path)

@measure_energy(handler=csv_handler)
def load_json(path):
    return pd.read_json(path)  


# I/O functions - WRITE
@measure_energy(handler=csv_handler)
def save_csv(df, path):
    return df.to_csv(path, index=False)

@measure_energy(handler=csv_handler)
def save_hdf(df, path, key):
    return df.to_hdf(path, key=key)

@measure_energy(handler=csv_handler)
def save_json(df, path):
    return df.to_json(path)  

###------------------------------------------###

# Handling missing data 
@measure_energy(handler=csv_handler)
def isna(df, cname):
    return df[cname].isna()

@measure_energy(handler=csv_handler)
def dropna(df):
    return df.dropna()

@measure_energy(handler=csv_handler)
def fillna(df, val):
    return df.fillna(val)

@measure_energy(handler=csv_handler)
def replace(df, cname, src, dest):
    return df[cname].replace(src, dest)

###------------------------------------------###

# Table operations
@measure_energy(handler=csv_handler)
def drop(df, cnameArray):
    return df.drop(columns=cnameArray)

@measure_energy(handler=csv_handler)
def groupby(df, cname):
    return df.groupby(cname)

@measure_energy(handler=csv_handler)
def merge(df1, df2, on=None):
    if(on):
        return pd.merge(df1, df2, on=on)
    else:
        return pd.merge(df1, df2)

@measure_energy(handler=csv_handler)
def sort(df, cname):
    return df.sort_values(by=[cname])

@measure_energy(handler=csv_handler)
def concat_dataframes(df1, df2):
    return pd.concat([df1, df2])

###--------------------------------------------###

# Statistical Operations

# count 
@measure_energy(handler=csv_handler)
def count(df):
    return df.count()

# sum
@measure_energy(handler=csv_handler)
def sum(df, cname):
    return df[cname].sum()

# mean
@measure_energy(handler=csv_handler)
def mean(df):
    return df.mean()

# min
@measure_energy(handler=csv_handler)
def min(df):
    return df.min()

# max
@measure_energy(handler=csv_handler)
def max(df):
    return df.max()

# unique
@measure_energy(handler=csv_handler)
def unique(df, cname):
    return df[cname].unique()

###--------------------------------------------###


print("Starting Retail Pandas Process...")
for i in range(10):
    # Input-output functions 
    df = load_csv(path='../datasets/onlineretail.csv')
    sleep()
    df = load_json(path='../datasets/onlineretail.json')   
    sleep()
    df = load_hdf(path='../datasets/onlineretail.h5')
    sleep()

    save_csv(df, f'df_onlineretail_pandas{i}.csv')
    sleep()
    save_json(df, f'df_onlineretail_pandas{i}.json')
    sleep()
    save_hdf(df, f'df_onlineretail_pandas{i}.h5', key='a')
    sleep()
    
    # Handling missing data
    df = pd.read_csv('../datasets/onlineretail.csv')
    sleep()
    isna(df, cname='Customer ID')
    sleep()
    dropna(df)
    sleep()
    fillna(df, val='0')
    sleep()
    replace(df, cname='Description', src='0', dest='N/A')
    sleep()

    # Table operations
    df_samp = pd.read_csv('../datasets/onlineretail.csv')
    sleep()
    drop(df, cnameArray=['InvoiceDate', 'StockCode'])
    sleep()
    groupby(df, cname='Country')
    sleep()
    concat_dataframes(df, df_samp)
    sleep()
    sort(df, 'Price')
    sleep()
    merge(df, df_samp)
    sleep()

    # Statistical operations
    df = pd.read_csv('../datasets/onlineretail.csv')
    sleep()
    count(df)
    sleep()
    sum(df, 'Quantity')
    sleep()
    mean(df['Price'])
    sleep()
    min(df['Price'])
    sleep()
    max(df['Price'])
    sleep()
    unique(df, 'Country')
    sleep()

    print(f"Finished {i+1} iterations.")

csv_handler.save_data()
print("Process ended...")
