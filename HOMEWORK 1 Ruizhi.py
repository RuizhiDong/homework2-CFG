#Q1
'''
import pandas_datareader as pdr
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

wb = openpyxl.Workbook()

wb.save('goog.xls')

api_key = '608a97378e2183f649746e9bb0acfe986fb683ef'

start = "2020-1-1"
end = "2021-1-1"

df = pdr.tiingo.TiingoDailyReader('GOOG', start=start, end=end, api_key=api_key)

goog = df.read()
print(goog)

excel_df = pd.read_excel('goog.xls')
excel_df.head()

excel_df.to_csv('goog_historical.csv', header = True)

goog.to_csv('goog_historical.csv', date_format='%Y-%m-%d')
saved_df = pd.read_csv('goog_historical.csv', header=0, index_col='date', parse_dates=True)

s_data = pd.read_csv("goog_historical.csv", usecols=['close', 'high', 'low'], encoding='gbk')
print(s_data)

S_list = pd.read_csv("goog_historical.csv")
S_list.head()

goog['close'].plot()

plt.show()

'''

#Q2
import pandas_datareader as pdr
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

wb = openpyxl.Workbook()

wb.save('msft.xls')

api_key = '608a97378e2183f649746e9bb0acfe986fb683ef'

start = "2020-1-1"
end = "2021-1-1"

df = pdr.tiingo.TiingoDailyReader('MSFT', start=start, end=end, api_key=api_key)

msft = df.read()
print(msft)

excel_df = pd.read_excel('msft.xls')
excel_df.head()

excel_df.to_csv('msft_historical.csv', header = True)

msft.to_csv('msft_historical.csv', date_format='%Y-%m-%d')
saved_df = pd.read_csv('msft_historical.csv', header=0, index_col='date', parse_dates=True)

s_data = pd.read_csv("msft_historical.csv", usecols=['close', 'high', 'low'], encoding='gbk')
print(s_data)

S_list = pd.read_csv("msft_historical.csv")
S_list.head()

msft['close'].plot()

plt.show()



