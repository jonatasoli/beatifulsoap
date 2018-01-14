from sqlalchemy.orm import mapper, relation
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from connection import CreateConnection


class CreateModel():
    metadata = MetaData()

    engine = CreateConnection.create()

    table_crypto = Table('table_crypto', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(100)),
        Column('market_cap', String(100)),
        Column('price', String(100)),
        Column('volume_24h', String(100)),
        Column('circulatins_supply', String(100)),
        Column('change_24h', String(100)),
        Column('prive_graph_7_days', String(100))
        )

    metadata.create_all(engine)

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
