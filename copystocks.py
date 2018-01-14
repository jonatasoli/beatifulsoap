import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from model import CryptoModel


class WebCrawlerCoinMarket(CryptoModel):

    def save_data():

        try:
            request = requests.get("https://coinmarketcap.com/", timeout=5)
        except requests.exceptions.RequestException as e:
            print (e)
            sys.exit(1)

        list_stocks = []
        crypto_stocks = CryptoModel()
        Session = sessionmaker(bind = engine)
        session = Session()


        request_html =request .content
        request_html = request.content
        soup = BeautifulSoup(request_html, "html.parser")

        body_html = soup.find("tbody")
        for row in body_html.findAll("tr"):
            cells = row.findAll("td")
            crypto_stocks.name = cells[1].text.strip(" \n")
            crypto_stocks.market_cap = cells[2].text.strip(" \n")
            crypto_stocks.price = cells[3].text.strip(" \n")
            crypto_stocks.volume_24h = cells[4].text.strip(" \n")
            crypto_stocks.circulatins_supply= cells[5].text.strip(" \n")
            crypto_stocks.change_24h = cells[6].text.strip(" \n")
            crypto_stocks.prive_graph_7_days = cells[7].find('img')['src']

            session.add(crypto_stock)

        session.commit()

        print("Stocks Create Succefull!")
