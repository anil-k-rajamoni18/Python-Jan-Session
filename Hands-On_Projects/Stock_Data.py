#import the library

import yfinance as yf

# company = yf.Ticker('MSFT')

# stock_data = company.histrory(period='lmo')

stock_data = yf.download(tickers='UBER', period='5d', interval='5m')
#

print(stock_data)