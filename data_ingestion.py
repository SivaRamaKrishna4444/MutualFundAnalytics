import pandas as pd
import os

data_folder = "data/raw"

files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

for file in files:
    print("\n" + "="*50)
    print("FILE:", file)

    df = pd.read_csv(os.path.join(data_folder, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())