# https://github.com/sharebook-kr/pykrx : pykrx 개발자 github

import pykrx # NAVER, KRX(한국거래소)에서 주가정보를 스크래핑하는 오픈소스 라이브러리
import time
from pykrx import stock
from pykrx import bond

#현재 시간을 구하여 presentTime에 저장
presentTime=time.strftime('%Y%m%d')
print("오늘 날짜", presentTime)


#현 시간때의 상장되어있는 모든 주식의 가격 출력 (매우 오래걸림)
def print_price_all_stocks():
    for ticker in stock.get_market_ticker_list():
        df = stock.get_market_ohlcv(presentTime) # 현재 시간의 
        stocks = stock.get_market_ticker_name(ticker)
        print(stock.get_market_ticker_name(ticker))
        print(df.loc[ticker])

#시장의 ticker와 그 ticker에 매치되는 종목 출력        
def print_name_and_ticker_all_stocks():
    for ticker in stock.get_market_ticker_list():
        stocks = stock.get_market_ticker_name(ticker)
        print(ticker, stocks)
        
#print_name_and_ticker_all_stocks()
#print_price_all_stocks()


#text
