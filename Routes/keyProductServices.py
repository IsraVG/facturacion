from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.keyProductServices import productServices
from Schemas.keyProductServices import KeyProductServices
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

keyProductServices = APIRouter()

@keyProductServices.get( "/keyProductServices", response_model=List[KeyProductServices], tags=["KeyProductServices"] )
def getKeyProductServices():
    return conn.execute( productServices.select() ).fetchall()

@keyProductServices.get( "/keyProductServices/{id}", response_model=KeyProductServices, tags=["KeyProductServices"] )
def getKeyProductService( id: int ):
    return conn.execute( productServices.select().where( productServices.c.id == id ) ).first()

@keyProductServices.post( "/keyProductServices", response_model=KeyProductServices, tags=["KeyProductServices"] )
def createKeyProductService( keySchema: KeyProductServices ):
    result = conn.execute( productServices.insert().values( keySchema.dict() ) )
    return conn.execute( productServices.select().where( productServices.c.id == result.lastrowid ) ).first()

@keyProductServices.delete( "/keyProductServices/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["KeyProductServices"] )
def deleteKeyProductService( id: int ):
    result = conn.execute( productServices.delete().where( productServices.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@keyProductServices.put( "/keyProductServices/{id}", response_model=KeyProductServices, tags=["KeyProductServices"] )
def updateCoin( id: int, keySchema: KeyProductServices ):
    conn.execute( productServices.update().values( keySchema.dict() ).where( productServices.c.id == id ) )
    return conn.execute( productServices.select().where( productServices.c.id == id ) ).first()
