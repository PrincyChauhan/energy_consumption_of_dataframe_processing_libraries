from pickletools import read_uint1
from random import sample
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

csv_handler = CSVHandler('online_retail.csv')
import time
import vaex as ve

def sleep():
    time.sleep(30)
    


# I/O functions - READ
@measure_energy(handler=csv_handler)
def load_csv(path):
    return ve.read_csv(path)

@measure_energy(handler=csv_handler)
def load_hdf(path):
    return ve.open(path)

@measure_energy(handler=csv_handler)
def load_json(path):
    return ve.from_json(path)

# I/O functions - WRITE
@measure_energy(handler=csv_handler)
def save_csv(df, path):
    return df.export_csv(path)

@measure_energy(handler=csv_handler)
def save_hdf(df, path, key='a'):
    return df.export(path)

@measure_energy(handler=csv_handler)
def save_json(df, path):
    return df.export_json(path)

###------------------------------------------###

# Missing data handling 
@measure_energy(handler=csv_handler)
def dropna(df):
    return df.dropna()

@measure_energy(handler=csv_handler)
def fillna(df, val):
    return df.fillna(val)

@measure_energy(handler=csv_handler)
def isna(df, cname):
    return df[cname].isna()

@measure_energy(handler=csv_handler)
def replace(df, cname, src, dest):
    return df[cname].str.replace(src, dest)    

###------------------------------------------###

# Table operations
# drop column
# groupby
# merge 
# transpose
# sort


@measure_energy(handler=csv_handler)
def drop(df, col_names=[]):
    df.drop(columns=col_names)

@measure_energy(handler=csv_handler)
def groupby(df, cname):
    return df.groupby(cname)

@measure_energy(handler=csv_handler)
def merge(df1, df2, on=None, lsuffix="_l"):
    if(on == None):
        return df1.join(df2, lsuffix="_l")
    else:
        return df1.join(df2, on=on, how='inner', lsuffix=lsuffix)

@measure_energy(handler=csv_handler)
def sort(df, cname):
    return df.sort(cname)

@measure_energy(handler=csv_handler)
def concat_dataframes(df1, df2):
    return ve.concat([df1, df2])

###--------------------------------------------###
# Statistical Operations
# min, max, mean, count, unique, correlation

# count 
@measure_energy(handler=csv_handler)
def count(df):
    return df.count()

# sum
@measure_energy(handler=csv_handler)
def sum(df, cname):
    return df.sum(cname)

# mean
@measure_energy(handler=csv_handler)
def mean(df):
    return df.mean()

# min
@measure_energy(handler=csv_handler)
def min(df):
    return df.min()

@measure_energy(handler=csv_handler)
def max(df):
    return df.max()

@measure_energy(handler=csv_handler)
def unique(df):
    return df.unique()

print("Starting online retail  Vaex Process...")
for i in  range(10):
    # Input Output functions
    df = load_csv(path='../datasets/onlineretail.csv')
    sleep()
    df = load_json(path='../datasets/onlineretail.json')
    sleep()
    df = load_hdf(path='../datasets/onlineretail.hdf5')
    sleep()

    save_csv(df, f'df_onlineretail_vaex_{i}.csv')
    sleep()
    save_json(df, f'df_onlineretail_vaex_{i}.json')
    sleep()
    save_hdf(df, f'df_onlineretail_vaex_{i}.hdf5')
    sleep()

    # --------------------------------------------------

    # Handling missing data
    df = ve.read_csv('../datasets/onlineretail.csv')
    sleep()
    isna(df, cname='Customer ID')
    sleep()
    dropna(df)
    sleep()
    fillna(df, val='Unknown')
    sleep()
    replace(df, cname='Description', src='?', dest='Unknown Item')
    sleep()

    # --------------------------------------------------
    # Table operations
    df = ve.read_csv('../datasets/onlineretail.csv')
    sleep()
    df_samp = ve.read_csv('../datasets/onlineretail.csv')
    sleep()
    drop(df, col_names=['Description', 'Country'])
    sleep()
    groupby(df, cname='Country')
    sleep()

    concat_dataframes(df, df_samp)
    sleep()

    sort(df, 'Quantity')
    sleep()
    merge(df, df_samp)
    sleep()

    # ------------------------------------------
    # Statistical operations
    df = ve.read_csv('../datasets/onlineretail.csv')
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
    unique(df['Invoice'])
    sleep()

    print(f"Finished iteration {i+1}")

print("Process Complete...")

csv_handler.save_data()
