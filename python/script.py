#Script to autorun at startup
from datetime import date
from nsepy import get_history
import pandas as pd
from datetime import date
from datetime import timedelta
from win10toast import ToastNotifier

lastTradingDay = date.today()

if(lastTradingDay.weekday==5):
    lastTradingDay= lastTradingDay - timedelta(days=1);

elif(lastTradingDay.weekday==6):
    lastTradingDay= lastTradingDay - timedelta(days=2);

print("Last trading day:", lastTradingDay)

frames=[]
stockList = ["ULTRACEMCO","HINDALCO","SBILIFE","LT","DRREDDY","SUNPHARMA","BAJAJFINSV","GRASIM","DIVISLAB","COALINDIA","TCS","SHREECEM","CIPLA","UPL","BPCL","KOTAKBANK","ONGC","HEROMOTOCO","JSWSTEEL","AXISBANK","WIPRO","ITC","POWERGRID","ADANIPORTS","HDFC","TATASTEEL","HDFCLIFE","TATAMOTORS","NTPC","HINDUNILVR","MARUTI","BHARTIARTL","TITAN","BAJFINANCE","BAJAJ-AUTO","SBIN","BRITANNIA","ICICIBANK","IOC","ASIANPAINT","RELIANCE","EICHERMOT","HDFCBANK","NESTLEIND","HCLTECH","TECHM","M&M","TATACONSUM","INDUSINDBK","INFY"]

for stock in stockList:
    temp = get_history(symbol=stock,start=lastTradingDay, end= lastTradingDay)
    #temp = get_history(symbol=stock,start= date(2021,12,14), end= date(2021,12,14)) #Format: yyyy,mm,dd

    frames.append(temp)

stocksDf=pd.concat(frames)
stocksDf.drop(["Series" , "VWAP" , "Volume" , "Turnover", "Trades", "Deliverable Volume"] , axis=1 , inplace=True)

def isHammer(df):
    if(df.iloc[6] >= df.iloc[2]): #If green candle
        if(
            (df.iloc[4] - df.iloc[2]) >= 2*(df.iloc[6] - df.iloc[2])  #If the lower wick is twice or more than body
            and
            (df.iloc[3] - df.iloc[6]) <= (0.2 * (df.iloc[6] - df.iloc[2])) #The higher wick is very small
        ):
            return True
        else:
            return False
        
    else: #If red candle
        if(
            (df.iloc[2] - df.iloc[4]) >= 2*(df.iloc[2] - df.iloc[6]) #If the lower wick is twice or more than body
            and
            (df.iloc[3] - df.iloc[2]) <= (0.2 * (df.iloc[2] - df.iloc[6])) #The higher wick is very small
        ):
            return True
        else:
            return False


def isInvertedHammer(df):
    if(df.iloc[6] - df.iloc[2]): #If candle is green
        if(
            (df.iloc[3] - df.iloc[6]) >= 2* (df.iloc[6] - df.iloc[2])
            and
            (df.iloc[2] - df.iloc[4]) <= 0.2 * (df.iloc[6] - df.iloc[2])
        ):
            return True;
        else:
            return False;
        
    else:
        if(
            (df.iloc[3] - df.iloc[2]) >= 2* (df.iloc[2] - df.iloc[6])
            and
            (df.iloc[6] - df.iloc[4]) <= 0.2 * (df.iloc[2] - df.iloc[6])
        ):
            return True;
        else:
            return False;       

answerList=[]
for i in range(len(stocksDf)):
    if isInvertedHammer(stocksDf.iloc[i]):
        answerList.append([str(stocksDf.iloc[i][0]) , "Inv Hammer"])
            
    if isHammer(stocksDf.iloc[i]):
        answerList.append([str(stocksDf.iloc[i][0]) , "Hammer"])

print(answerList)

if(len(answerList)>0):
    notif= ToastNotifier();
    notif.show_toast("Nifty Hammer", f"We found {len(answerList)} stocks for you today" , icon_path= "C:/Users/rugve/stock-project/web/scriptIcon.ico", duration=15)