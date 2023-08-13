from sqlalchemy import create_engine, MetaData

engine = create_engine( 'mysql+mysqlconnector://root:aztektec321@192.168.1.7/facturacion' )

meta = MetaData()

conn = engine.connect()
