from sqlalchemy import create_engine


class CreateConnection():
    def create():
        engine = create_engine(
            'mysql://db_html:BNN5BgC2gBsZJ46N@soap.czepwkmln8k1.sa-east-1.rds.amazonaws.com/dbsoap'
            )
        return engine

