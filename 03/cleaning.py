import seaborn as sns
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import os


def handle_missing_values(df):
    # age            177
    # embarked         2
    # deck           688
    # embark_town      2
    # dtype: int64

    df = df.copy()
    df["age"] = df["age"].fillna(df["age"].median())
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])
    df = df.drop("deck", axis=1)

    return df


def remove_duplicates(df):
    df = df.copy()
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"\nRemoved {before - after} duplicate rows.")
    return df


def normalize_data(df):
    # MinMax scaling - [0, 1]
    df = df.copy()
    scaler = MinMaxScaler()
    df["fare_normalized"] = scaler.fit_transform(df[["fare"]])
    return df


def standardize_data(df):
    # Standard scaling - mean 0, std 1
    df = df.copy()
    standardizer = StandardScaler()
    df["age_standardized"] = standardizer.fit_transform(df[["age"]])
    return df


def preview_data(df, name="Titanic Dataset"):
    print(f"\n=== {name} Preview ===")
    print("Shape:", df.shape)
    print("\nHead: ")
    print(df.head())
    print("\nInfo: ")
    print(df.info())
    print("\nDescribe: ")
    print(df.describe(include="all"))


def check_missing_values(df):
    print("\nMissing:")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values found")


print("Loading Titanic dataset and saving to CSV file...")
if not os.path.exists("data"):
    os.makedirs("data")
    print("Created 'data' directory.")
else:
    print("'data' directory already exists.")
    df = sns.load_dataset("titanic")
    df.to_csv("data/titanic.csv", index=False)
    print("Titanic dataset loaded and saved to 'data/titanic.csv'.")
    preview_data(df, name="Original Titanic Dataset")
    check_missing_values(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    check_missing_values(df)
    df = normalize_data(df)
    df = standardize_data(df)
    preview_data(df, name="Cleaned Titanic Dataset")
