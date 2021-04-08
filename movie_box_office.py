import os
import pandas as pd
from matplotlib import pyplot as plt
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, 'data')
correct_extension = [file for file in os.listdir(DATA_DIR) if file.endswith('.csv')]
entire_data = []
for filename in correct_extension:
    csv_path = os.path.join(DATA_DIR, filename)
    this_csv = pd.read_csv(csv_path)
    this_csv['filename']= filename[:-4]
    entire_data.append(this_csv)

big_data = pd.concat(entire_data)
big_data.to_csv('data_set', index = False)
data = pd.read_csv('data_set')

data_to_clean = ['Worldwide','Domestic', 'Foreign']


def currency_str_to_int(current_val):
    current_val = current_val.replace('$', '').replace(',','')
    try:
        current_val = int(current_val)
    except:
        current_val = 0
    return current_val


def clean_col(row):
    for col in data_to_clean:
        current_val = row[col]
        row[col] = currency_str_to_int(current_val)
    return row


cl_data = data.apply(clean_col, axis = 1)

cl_data.to_csv('cl_date.csv')

print(cl_data.iloc[1])