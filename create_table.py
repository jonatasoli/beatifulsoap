from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData


class CreateModel():
    metadata = MetaData()

    engine = create_engine(
        'mysql://db_html:BNN5BgC2gBsZJ46N@soap.czepwkmln8k1.sa-east-1.rds.amazonaws.com/dbsoap'
        )

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
