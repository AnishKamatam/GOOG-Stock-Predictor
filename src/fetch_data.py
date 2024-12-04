import os
import yfinance as yf
import pandas as pd

def fetch_google_data(start_date="2010-01-01", end_date="2024-12-01"):
    data_folder = "data"

    print(f"Fetching Google stock data from {start_date} to {end_date}...")
    
    # Change stock symbol to 'GOOG' for Google stock
    google_data = yf.download("GOOG", start=start_date, end=end_date)

    file_path = os.path.join(data_folder, "google_stock_data.csv")
    google_data.to_csv(file_path)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    fetch_google_data()