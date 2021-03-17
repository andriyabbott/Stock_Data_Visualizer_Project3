import requests, pygal, lxml
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries 
import pandas as pd

API_URL = "https://www.alphavantage.co/query"
API_KEY = "X0AWJSYKTOKX2F5E"

def getData(symbol,timeSeries,startDate,endDate):

    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if timeSeries == '1':
        data, meta_data = ts.get_intraday(symbol=symbol, interval='15min', outputsize='full')
    if timeSeries == '2':
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
    if timeSeries == '3':
        data, meta_data = ts.get_weekly(symbol=symbol)
    if timeSeries == '4':
        data, meta_data = ts.get_monthly(symbol=symbol)
    data_date_changed = data[:startDate]
    print(data_date_changed)


def lineChart(symbol, beginDate, endDate):
    from datetime import datetime, timedelta
    line_chart = pygal.Line(x_label_rotation=20)
    line_chart.title = 'Stock Data for {}: {} to {}'.format(symbol, beginDate, endDate)
    line_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
        datetime(2013, 1, 2), datetime(2013, 1, 12), datetime(2013, 2, 2), datetime(2013, 2, 22)])
    line_chart.add("Open", [300, 412, 823, 672])
    line_chart.add("High", [300, 412, 823, 672])
    line_chart.add("Low", [300, 412, 823, 672])
    line_chart.add("Close", [300, 412, 823, 672])
    line_chart.render()
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
            getData(symbol,timeSeries,startDate,endDate)
            
            again = input("Would you like to view more stock data? Press 'y' to continue: ")
            if (again.lower() != "y"):
                break
        except Exception as err:
            print (err)
            

main()
