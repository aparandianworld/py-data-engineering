import pandas as pd
from ydata_profiling import ProfileReport
import os
from datetime import datetime

try:
    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    df = None

    if not os.path.exists("data/tips.csv"):
        url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
        df = pd.read_csv(url)
        df.to_csv("data/tips.csv", index=False)
    else:
        df = pd.read_csv("data/tips.csv")

    print(df.head())

    profile = ProfileReport(df, title="Tips Dataset Profile", explorative=True)
    profile.to_file(
        f"reports/tips_dataset_profile_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    )

except Exception as e:
    print(f"Error reading the dataset: {e}")
    exit(1)
