import os
import pandas as pd
import yfinance as yf
from datetime import datetime

def fetch_sp500_data(start_date="2010-01-01", end_date=None, data_folder="data"):
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    file_path = os.path.join(data_folder, "sp500_data.csv")
    print(f"Fetching S&P 500 data from {start_date} to {end_date}...")

    sp500_data = yf.download("^GSPC", start=start_date, end=end_date)

    os.makedirs(data_folder, exist_ok=True)

    if os.path.exists(file_path):
        print(f"Reading existing data from {file_path}")
        existing_data = pd.read_csv(file_path)

        if "Date" not in existing_data.columns:
            print("Warning: 'Date' column not found in existing data. Adding 'Date' column.")
            existing_data["Date"] = pd.to_datetime(existing_data.index)

        existing_data["Date"] = pd.to_datetime(existing_data["Date"])
        sp500_data.reset_index(inplace=True)
        combined_data = pd.concat([existing_data, sp500_data]).drop_duplicates(subset="Date")
    else:
        sp500_data.reset_index(inplace=True)
        combined_data = sp500_data

    combined_data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    fetch_sp500_data()
