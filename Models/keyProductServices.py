from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

productServices = Table( "clave_productos_servicios", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "code", String( 10 ) ),
                Column( "description", String( 200 ) ),
                Column( "status", TINYINT(1) )
            )