from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.unitKey import unitKey as unitModel
from Schemas.unitKey import UnitKey
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

unitKey = APIRouter()

@unitKey.get( "/unitKey", response_model=List[UnitKey], tags=["UnitKey"] )
def getUnitKey():
    return conn.execute( unitModel.select() ).fetchall()

@unitKey.get( "/unitKey/{id}", response_model=UnitKey, tags=["UnitKey"] )
def getUnit( id: int ):
    return conn.execute( unitModel.select().where( unitModel.c.id == id ) ).first()

@unitKey.post( "/unitKey", response_model=UnitKey, tags=["UnitKey"] )
def createUnitKey( unitSchema: UnitKey ):
    result = conn.execute( unitModel.insert().values( unitSchema.dict() ) )
    return conn.execute( unitModel.select().where( unitModel.c.id == result.lastrowid ) ).first()

@unitKey.delete( "/unitKey/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["UnitKey"] )
def deleteUnitKey( id: int ):
    result = conn.execute( unitModel.delete().where( unitModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@unitKey.put( "/unitKey/{id}", response_model=UnitKey, tags=["UnitKey"] )
def updateUnitKey( id: int, unitSchema: UnitKey ):
    conn.execute( unitModel.update().values( unitSchema.dict() ).where( unitModel.c.id == id ) )
    return conn.execute( unitModel.select().where( unitModel.c.id == id ) ).first()
