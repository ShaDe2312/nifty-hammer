from datetime import date
from nsepy import get_history
import pandas as pd
import eel
from datetime import date
from datetime import timedelta

eel.init('C:/Users/rugve/stock-project/web')

lastTradingDay = date.today()
print("Today is: ", lastTradingDay.weekday())
if(lastTradingDay.weekday()==5):
    lastTradingDay= lastTradingDay - timedelta(days=1);

elif(lastTradingDay.weekday()==6):
    lastTradingDay= lastTradingDay - timedelta(days=2);

print("Last trading day:", lastTradingDay)

@eel.expose
def abcd(): #Function only for testing
    string="JS is nice"
    return string;

@eel.expose
def hammerList():
    frames=[]
    stockList = ["ULTRACEMCO","HINDALCO","SBILIFE","LT","DRREDDY","SUNPHARMA","BAJAJFINSV","GRASIM","DIVISLAB","COALINDIA","TCS","SHREECEM","CIPLA","UPL","BPCL","KOTAKBANK","ONGC","HEROMOTOCO","JSWSTEEL","AXISBANK","WIPRO","ITC","POWERGRID","ADANIPORTS","HDFC","TATASTEEL","HDFCLIFE","TATAMOTORS","NTPC","HINDUNILVR","MARUTI","BHARTIARTL","TITAN","BAJFINANCE","BAJAJ-AUTO","SBIN","BRITANNIA","ICICIBANK","IOC","ASIANPAINT","RELIANCE","EICHERMOT","HDFCBANK","NESTLEIND","HCLTECH","TECHM","M&M","TATACONSUM","INDUSINDBK","INFY"]

    for stock in stockList:
        #temp = get_history(symbol=stock,start=lastTradingDay, end= lastTradingDay)
        temp = get_history(symbol=stock,start= date(2022,1,20), end= date(2022,1,20)) #Format: yyyy,mm,dd

        frames.append(temp)

    stocksDf=pd.concat(frames)
    stocksDf.drop(["Series" , "VWAP" , "Volume" , "Turnover", "Trades", "Deliverable Volume"] , axis=1 , inplace=True)

    # On a daily chart,each candlestick details a single day’s trading. It has three basic features:

    # The body, which represents the open-to-close range
    # The wick, or shadow, that indicates the intra-day high and low
    # The colour, which reveals the direction of market movement – a green (or white) body indicates a price increase, 
    # while a red (or black) body shows a price decrease

    # Hammer
    # The hammer candlestick pattern is formed of a short body with a long lower wick, and is found at the bottom of a downward trend.

    """
    Symbol: 0
    Prev Close:1
    Open:2
    High:3
    Low:4
    Last:5
    Close:6
    """

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
    return answerList;

eel.start('C:/Users/rugve/stock-project/web/main.html' , mode='chrome' , size = (400,370))