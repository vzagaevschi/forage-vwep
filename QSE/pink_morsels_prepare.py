import pandas as pd
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./data/output.csv"

frames = []

# open csv files for reading
for file_name in os.listdir(DATA_DIRECTORY):
    frames.append(pd.read_csv(f"{DATA_DIRECTORY}/{file_name}"))

# merged files
df = pd.concat(frames)

# filtered data
dff = df.query("product == 'pink morsel'")

# create new product column
dff['sales'] = dff['price'].str.replace('$', '').astype(float) * dff['quantity']

# removed useless columns
dff.drop(columns=['product', 'price', 'quantity'], axis=1, inplace=True)

# reorder columns
dff = dff[["sales", "date", "region"]]

# write data to output file
dff.to_csv(OUTPUT_FILE_PATH, index=False)
