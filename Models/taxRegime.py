from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from Config.db import meta

taxRegime = Table( "regimen_fiscal", meta,
                Column( "id", Integer(), primary_key=True ),
                Column( "code", String( 4 ) ),
                Column( "description", String( 100 ) ),
                Column( "physical_person", TINYINT(1) ),
                Column( "moral_person", TINYINT(1) ),
                Column( "status", TINYINT(1) )
            )