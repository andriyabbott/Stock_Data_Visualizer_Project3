import requests, pygal, lxml
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries 
import pandas as pd

API_URL = "https://www.alphavantage.co/query"
API_KEY = "X0AWJSYKTOKX2F5E"

def getData(symbol,timeSeries,chartType, startDate,endDate):

    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if timeSeries == '1':
        data, meta_data = ts.get_intraday(symbol=symbol, interval='60min', outputsize='full')
        f = 'H'
    if timeSeries == '2':
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
        f = 'D'
    if timeSeries == '3':
        data, meta_data = ts.get_weekly(symbol=symbol)
        f = 'W'
    if timeSeries == '4':
        data, meta_data = ts.get_monthly(symbol=symbol)
        f = 'M'

    data_date_changed = data[endDate:startDate]

    if chartType == "2":
        line_chart = pygal.Line(x_label_rotation=20, spacing=80)
        line_chart.title = 'Stock Data for {}: {} to {}'.format(symbol, startDate, endDate)
        
        line_chart.x_labels= pd.date_range(start=startDate, end=endDate, freq= f)
        
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        line_chart.render_in_browser()
        
    if chartType == "1":
        line_chart = pygal.Bar(x_label_rotation=20, spacing=80)
        line_chart.title = 'Stock Data for {}:  {} to {}'.format(symbol, startDate, endDate)
        line_chart.x_labels = pd.date_range(start=startDate, end=endDate, freq= f)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        line_chart.render_in_browser()


def main():

    while(True):
        try:
            
            print("Stock Data Visualizer")
            print("-------------------------")
            symbol = input("Enter the stock symbol you are looking for: ")
            
            print("\nChart Type:")
            print("-------------------------")
            print("1. Bar\n2. Line\n")
            chartType = input("Enter the chart type you want (1,2): ")
            print("\nSelect the time series of the chart you want to generate")
            print("-------------------------------------------------------------")
            print("1.Intrady\n2. Daily\n3. Weekly\n4. Monthly")
            timeSeries = input("Enter time series option (1,2,3,4): ")
            startDate = input("\nEnter the start date (YYYY-MM-DD): ")
            endDate = input("\nEnter the end date (YYYY-MM-DD): ")
            getData(symbol,timeSeries,chartType, startDate,endDate)

            
            again = input("Would you like to view more stock data? Press 'y' to continue: ")
            if (again.lower() != "y"):
                break
        except Exception as err:
            print (err)
            

main()
