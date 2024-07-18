# Stocks-Project

## Prerequisites

python3 -m venv venv
.\venv\Scripts\activate.bat

pip install -r requirements.txt

## Goals

1. Have user enter a stock ticker or name
2. Run that stock through a Machine Learning program that will interpret the balance sheet of that stock and determine if it is a good buy or not
3. Create a website that will have a place for the user to enter the stock name or ticker and will display the results

## Crieria for Learning Model

### A Quanitative Analysis to help users pick a stock based on the financials:

- Note: Only works on individual company stocks, not stocks with portfolio holdings in other companies

1. Total Current Assets / Total Curent Liabilities > 1, means they are able to pay off their short term debt
2. Operating Income / Total Revenue > .15
3. Free Cash Flow Inceasing over the past few years
