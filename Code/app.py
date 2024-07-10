import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from yfinance.exceptions import YFException
from requests.exceptions import HTTPError






found = False

#loop that will continually ask the user to input their ticker (update to take names as well as tickers)
while(not found):

    ticker = input("What is the ticker of the stock you would like to analyze?: ")
    print(ticker)

    stock = yf.Ticker(ticker)

    try:

        balance_sheet = stock.balance_sheet

        if(balance_sheet.empty):
            raise ValueError("Stock info not found, please recheck your ticker symbol")
        else:
            found = True
            print(balance_sheet)

    except ValueError as ve:
        print("Stock information not found, please check if the ticker was entered correctly.")
    
    except HTTPError as http_err:
        if http_err.response.status_code == 404:
            print("HTTP Error: 404 Not Found. The ticker symbol may be incorrect")
        else:
            print(f"HTTP Error occurred: {http_err}")



    














