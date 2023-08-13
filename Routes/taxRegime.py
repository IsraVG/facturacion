from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.taxRegime import taxRegime as regimeModel
from Schemas.taxRegime import TaxRegime
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

taxRegime = APIRouter()

@taxRegime.get( "/taxRegime", response_model=List[TaxRegime], tags=["TaxRegime"] )
def getTaxRegime():
    return conn.execute( regimeModel.select() ).fetchall()

@taxRegime.get( "/taxRegime/{id}", response_model=TaxRegime, tags=["TaxRegime"] )
def getRegime( id: int ):
    return conn.execute( regimeModel.select().where( regimeModel.c.id == id ) ).first()

@taxRegime.post( "/taxRegime", response_model=TaxRegime, tags=["TaxRegime"] )
def createTaxRegime( regimeSchema: TaxRegime ):
    result = conn.execute( regimeModel.insert().values( regimeSchema.dict() ) )
    return conn.execute( regimeModel.select().where( regimeModel.c.id == result.lastrowid ) ).first()

@taxRegime.delete( "/taxRegime/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["TaxRegime"] )
def deleteTaxRegime( id: int ):
    result = conn.execute( regimeModel.delete().where( regimeModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@taxRegime.put( "/taxRegime/{id}", response_model=TaxRegime, tags=["TaxRegime"] )
def updateTaxRegime( id: int, regimeSchema: TaxRegime ):
    conn.execute( regimeModel.update().values( regimeSchema.dict() ).where( regimeModel.c.id == id ) )
    return conn.execute( regimeModel.select().where( regimeModel.c.id == id ) ).first()
