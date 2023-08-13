from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.expedition import expedition as expeditionModel
from Schemas.expedition import Expedition
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

expedition = APIRouter()

@expedition.get( "/expedition", response_model=List[Expedition], tags=["Expedition"] )
def getExpedition():
    return conn.execute( expeditionModel.select() ).fetchall()

@expedition.get( "/expedition/{id}", response_model=Expedition, tags=["Expedition"] )
def getExp( id: int ):
    return conn.execute( expeditionModel.select().where( expeditionModel.c.id == id ) ).first()

@expedition.post( "/expedition", response_model=Expedition, tags=["Expedition"] )
def createExpedition( expeditionSchema: Expedition ):
    result = conn.execute( expeditionModel.insert().values( expeditionSchema.dict() ) )
    return conn.execute( expeditionModel.select().where( expeditionModel.c.id == result.lastrowid ) ).first()

@expedition.delete( "/expedition/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Expedition"] )
def deleteExpedition( id: int ):
    result = conn.execute( expeditionModel.delete().where( expeditionModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@expedition.put( "/expedition/{id}", response_model=Expedition, tags=["Expedition"] )
def updateExpedition( id: int, expeditionSchema: Expedition ):
    conn.execute( expeditionModel.update().values( expeditionSchema.dict() ).where( expeditionModel.c.id == id ) )
    return conn.execute( expeditionModel.select().where( expeditionModel.c.id == id ) ).first()
