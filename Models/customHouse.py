from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

customHouse = Table( "aduana", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "code", String( 5 ) ),
                Column( "description", String( 100 ) ),
                Column( "status", TINYINT(1) )
            )