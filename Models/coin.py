from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

coin = Table( "moneda", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "code", String( 4 ) ),
                Column( "description", String( 100 ) ),
                Column( "decimals", TINYINT(2) ),
                Column( "status", TINYINT(1) )
            )