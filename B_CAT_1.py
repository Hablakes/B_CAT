import yfinance as yf


msft = yf.Ticker("MSFT")

msft.info

msft.dividends

msft.splits

msft.financials

print(msft.balance_sheet)

