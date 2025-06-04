import pandas as pd
import os
from datetime import datetime

# Your folder path
folder = r"C:\Users\Abhinav Namburi\Downloads\effects-of-covid-19-on-hospital-utilization-trends-eqixh7u6"

# List of files
files = [
    "hospital-utilization-trends.csv",
    "utilization-trends-by-health-category.csv",
    "in-hospital-mortality-trends-by-health-category.csv",
    "in-hospital-mortality-trends-by-diagnosis-type.csv",
    "in-hospital-mortality-trends-by-secondary-diagnosis.csv"
]

# Try to convert dates using multiple formats
def try_parse_date(date_str):
    formats = ["%b-%y", "%b-%Y", "%m/%Y", "%m-%Y", "%Y-%m", "%m/%d/%Y"]
    for f in formats:
        try:
            return datetime.strptime(date_str.strip(), f)
        except:
            pass
    return None

# Loop and clean each file
for filename in files:
    print("Cleaning:", filename)

    path = os.path.join(folder, filename)
    df = pd.read_csv(path)

    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    if "date" in df.columns:
        df["date_parsed"] = df["date"].astype(str).apply(try_parse_date)

    if "count" in df.columns:
        df = df.dropna(subset=["date_parsed", "count"])
        df["count"] = pd.to_numeric(df["count"], errors="coerce")
        df = df.dropna(subset=["count"])
        df["count"] = df["count"].astype(int)

    df["year"] = df["date_parsed"].dt.year
    df["month"] = df["date_parsed"].dt.month
    df["quarter"] = df["date_parsed"].dt.to_period("Q").astype(str)

    output_path = os.path.join(folder, "cleaned_" + filename)
    df.to_csv(output_path, index=False)

    print("Saved to:", output_path)
