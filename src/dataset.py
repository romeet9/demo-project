import os
import pandas as pd


def load_and_replace_dataset():
    file_name = "daily-bike-share.csv"
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", file_name)
    df = pd.read_csv(file_path)
    # Perform any modifications to the DataFrame here
    df.to_csv(file_path, index=False)
    return df


print(load_and_replace_dataset())
