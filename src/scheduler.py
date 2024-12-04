import schedule
import time
from fetch_data import fetch_sp500_data

def job():
    print("Fetching latest S&P 500 data...")
    fetch_sp500_data(start_date="2010-01-01")

# Schedule the job
schedule.every().day.at("06:00").do(job)

print("Scheduler started. Waiting for tasks...")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)  # Avoid CPU overuse
except KeyboardInterrupt:
    print("\nScheduler stopped.")

