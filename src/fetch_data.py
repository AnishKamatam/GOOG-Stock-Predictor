import os
import yfinance as yf
import pandas as pd

def fetch_sp500_data(start_date="2010-01-01", end_date="2024-12-01"):
    data_folder = "data"

    print(f"Fetching S&P 500 data from {start_date} to {end_date}...")
 
    sp500_data = yf.download("^GSPC", start=start_date, end=end_date)

    file_path = os.path.join(data_folder, "sp500_data.csv")
    sp500_data.to_csv(file_path)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    fetch_sp500_data()
