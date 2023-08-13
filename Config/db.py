from sqlalchemy import create_engine, MetaData

engine = create_engine( 'mysql+mysqlconnector://root:FactV4.0@localhost/facturacion' )

meta = MetaData()

conn = engine.connect()
