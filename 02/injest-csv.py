import pandas as pd
import os

path = "data/tips.csv"

if not os.path.exists(path):
    print("Error: data file does not exist.")
    exit(1)

try:
    df = pd.read_csv(path)
    print(df.info())
    print(df.describe())
    print(df.head())

except Exception as e:
    print(f"Error reading the dataset: {e}")
    exit(1)
