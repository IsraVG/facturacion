from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

typeFactor = Table( "tipo_factor", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "description", String( 10 ) ),
                Column( "status", TINYINT(1) )
            )