## Overview

An Empirical Study on Energy Usage Patterns of Different Variants of Data Processing Libraries

## Prerequisites

Ensure that you have Python installed on your machine, along with `pip` for package management.

### Required Libraries and Versions

To run this project, you need specific versions of the following libraries:

- `pandas==2.2.2` and `pandas==2.1.4`
- `vaex==4.17.0` and `vaex==4.16.0`
- `scikit-learn==1.5.1` and `scikit-learn==1.5.0`
- `numpy==1.26.4` and `numpy==1.24.4`

You can install these required libraries by running:

```bash
pip install pandas==2.2.2
pip install pandas==2.1.4
pip install vaex==4.17.0
pip install vaex==4.16.0
pip install scikit-learn==1.5.1
pip install scikit-learn==1.5.0
pip install numpy==1.26.4
pip install numpy==1.24.4
```

### Generate HDF5 Files

First, navigate to the datasets folder and run the script to generate HDF5 files from the CSV datasets:

```
cd datasets
python adult_drug_generate_hdfs.py
```

This will create HDF5 files for the adult and drug datasets. Repeat this step for any additional datasets, change in adult_drug_generate_hdfs.py accordingly

### Running Analysis Scripts

After generating the HDF5 files, navigate to the scripts folder to run the analysis scripts:

```
cd scripts
```

Execute each analysis script to measure energy usage for different library versions. For example, to measure energy usage for pandas on the adult dataset, run:

```
python measure_adult_pandas.py
```

Repeat this process for each script provided, adjusting as necessary for each library version.

Each script generates results and stores them in a final CSV file with aggregated metrics across the different library.

### Folder Structure

`datasets`: Contains the original CSV files and JSON file and scripts for generating HDF5 files.

###

`scripts`: Contains analysis scripts to evaluate energy usage for various library.
