# Stocks-Project

## Prerequisites

1. create the virtual encvironment
   python3 -m venv venv

2. activate the venv
   .\venv\Scripts\activate.ps1 (for powershell)

   .\venv\Scripts\activate.bat (for cmdline)

   can also just try running activate if neither work

(if your system says you can run scripts, run:
Get-ExecutionPolicy -Scope CurrentUser
if it is restricted or undefined, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)

3. install requirements
   pip install -r requirements.txt

## Goals

1. Have user enter a stock ticker or name
2. Run that stock through a Machine Learning program that will interpret the balance sheet of that stock and determine if it is a good buy or not
3. Create a website that will have a place for the user to enter the stock name or ticker and will display the results

## Crieria for Learning Model

### A Quanitative Analysis to help users pick a stock based on the financials:

- Note: Only works on individual company stocks, not stocks with portfolio holdings in other companies

1. Total Current Assets / Total Curent Liabilities > 1 (means they are able to pay off their short term debt)
2. Operating Income / Total Revenue > .15 (company's revenue can support their daily operations)
3. Free Cash Flow Inceasing over the past few years
4. Gross Profit/ Total Revenue > .2 (shows that this stock has a good profit margin ratio)
5. .75 < Total Capital / Total Revenue > 1.5 (Good price to sales ratio)
