from sqlalchemy.orm import mapper, relation
from create_table import CreateModel


class CryptoModel(CreateModel):

    def __repr__(self):
        name = self.name
        market_cap = self.market_cap
        price = self.price
        volume_24h = self.volume_24h
        circulations_supply = self.circulations_supply
        change_24h = self.change_24h
        prive_graph_7_days = self.prive_graph_7_days

mapper(CryptoModel, CreateModel.table_crypto)
