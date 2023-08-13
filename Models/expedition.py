from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

expedition = Table( "expedicion", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "code", String( 2 ) ),
                Column( "description", String( 20 ) ),
                Column( "status", TINYINT(1) )
            )