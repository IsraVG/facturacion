from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.taxation import taxation as taxationModel
from Schemas.taxation import Taxation
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

taxation = APIRouter()

@taxation.get( "/taxation", response_model=List[Taxation], tags=["Taxation"] )
def getTaxation():
    return conn.execute( taxationModel.select() ).fetchall()

@taxation.get( "/taxation/{id}", response_model=Taxation, tags=["Taxation"] )
def getTax( id: int ):
    return conn.execute( taxationModel.select().where( taxationModel.c.id == id ) ).first()

@taxation.post( "/taxation", response_model=Taxation, tags=["Taxation"] )
def createTaxation( taxationSchema: Taxation ):
    result = conn.execute( taxationModel.insert().values( taxationSchema.dict() ) )
    return conn.execute( taxationModel.select().where( taxationModel.c.id == result.lastrowid ) ).first()

@taxation.delete( "/taxation/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Taxation"] )
def deleteTaxation( id: int ):
    result = conn.execute( taxationModel.delete().where( taxationModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@taxation.put( "/taxation/{id}", response_model=Taxation, tags=["Taxation"] )
def updateTaxation( id: int, taxationSchema: Taxation ):
    conn.execute( taxationModel.update().values( taxationSchema.dict() ).where( taxationModel.c.id == id ) )
    return conn.execute( taxationModel.select().where( taxationModel.c.id == id ) ).first()
