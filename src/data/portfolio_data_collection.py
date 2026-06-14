import os
import logging
from datetime import datetime, timedelta
import time
#import timedelta
import pandas as pd
import yfinance as yf


logging.basicConfig(
    filename = "logfile.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

tickers = ["AAPL", "MSFT", "AMZN", "TSLA", "GOOGL", "META", "NVDA", "JPM", "WMT", "NFLX"]

end_date = datetime.today()
start_date = end_date - timedelta(days = 5*365)

portfolio_data = pd.DataFrame()

logging.info("downloading stock data...")
start = time.time()
for ticker in tickers:
    stock_data = yf.download(ticker, start = start_date, end = end_date, auto_adjust=False)
    #print(stock_data.columns)
    portfolio_data[ticker] = stock_data["Adj Close"]
    portfolio_data['Date'+f'_{ticker}'] = stock_data.index.date
end = time.time()
logging.info(f"Downloding Completed!.time taken : {round(end - start,2)} ms")


os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Stock Portfolio Performance Optimization/data/raw")
logging.info(f"Saving dataset...")
portfolio_data.to_csv("Portfolio_data.csv", index = False)
logging.info(f"dataset saved with file path : {os.getcwd()}")




