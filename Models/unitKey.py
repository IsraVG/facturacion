from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

unitKey = Table( "clave_unidad", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "code", String( 5 ) ),
                Column( "description", String( 150 ) ),
                Column( "note", String( 700 ) ),
                Column( "status", TINYINT(1) )
            )