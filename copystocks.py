import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from model import CryptoModel
from connection import CreateConnection
from sqlalchemy import create_engine


class WebCrawlerCoinMarket():


    def crawler_coins():

        request = WebCrawlerCoinMarket.capture_request()
        request_html = request.content
        soup = BeautifulSoup(request_html, "html.parser")
        WebCrawlerCoinMarket.save_data(soup)

        print("Stocks Create Succefull!")


    def capture_request():
        try:
            request = requests.get("https://coinmarketcap.com/", timeout=5)
        except requests.exceptions.RequestException as e:
            print (e)
            sys.exit(1)
        return request


    def save_data(soup):
        engine = CreateConnection.create()
        crypto_stocks = CryptoModel()
        Session = sessionmaker(bind = engine)
        session = Session()
        body_html = soup.find("tbody")
        for row in body_html.findAll("tr"):
            cells = row.findAll("td")
            crypto_stocks.name = cells[1].text.strip(" \n")
            crypto_stocks.market_cap = cells[2].text.strip(" \n")
            crypto_stocks.price = cells[3].text.strip(" \n")
            crypto_stocks.volume_24h = cells[4].text.strip(" \n")
            crypto_stocks.circulations_supply= cells[5].text.strip(" \n")
            crypto_stocks.change_24h = cells[6].text.strip(" \n")
            crypto_stocks.prive_graph_7_days = cells[7].find('img')['src']

            session.add(crypto_stocks)
            session.commit()

            crypto_stocks = CryptoModel()
