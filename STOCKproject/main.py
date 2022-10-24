import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "aa61fca85a8644a692f55990f14c04f3"
ALPHA_KEY = "8W8MS2UEC8CJWZPP"
SSID_ACC_TWILIO = "AC4e6c06965942760b7c3dce9249e6f5fd"
AUTH_TOKEN_TWILIO = "651e21293166da1802199a13bf444b73"
MY_TWILIO_NUMBER = "+15713832810"


def stock_price():
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': ALPHA_KEY,
    }
    response = requests.get(url=STOCK_ENDPOINT, params=parameters).json()
    # print(response)
    day_before = response['Time Series (Daily)']['2022-10-19']['1. open']
    day_today = response['Time Series (Daily)']['2022-10-20']['1. open']
    open_yesterday = float(day_before)
    open_today = float(day_today)
    percentage = ((open_today - open_yesterday) / open_yesterday * 100)
    percentage = round(percentage, 2)
    difference = f"\n{COMPANY_NAME} {percentage}%"
    return difference


def news():
    parameters = {
        'q': STOCK,
        'from': '2022-10-20',
        'apikey': NEWS_KEY,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=parameters).json()
    articles = response['articles'][0:3]
    first_news = f"Headline: {articles[0]['title']}\nbrief: {articles[0]['description']}"
    second_news = f"Headline: {articles[1]['title']}\nbrief: {articles[1]['description']}"
    third_news = f"Headline: {articles[2]['title']}\nbrief: {articles[2]['description']}"
    news = f"{first_news}\n\n{second_news}\n\n{third_news}"
    return news


def send_sms(stock_price, news):
    client = Client(SSID_ACC_TWILIO, AUTH_TOKEN_TWILIO)
    message = client.messages \
        .create(
        body=f"{stock_price()}\n{news()}",
        from_=MY_TWILIO_NUMBER,
        to='+48515711024'
    )

    print(message.sid)


send_sms(stock_price, news)