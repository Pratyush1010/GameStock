import yfinance as yf
from datetime import date
def load_data(stock, stocks):
    START = "2022-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")
    data = yf.download(stocks[stock], START, TODAY)
    data.reset_index(inplace=True)
    return data

def load_fast_info(stock, stocks):
    data = yf.Ticker(stocks[stock])
    data = data.get_fast_info()
    # Create a table to display stock metrics
    data_table = {elem:data.get(elem) for elem in data}
    return data_table 