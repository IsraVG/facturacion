from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.customHouse import customHouse as customHouseModel
from Schemas.customHouse import CustomHouse
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

customHouse = APIRouter()

@customHouse.get( "/customHouse", response_model=List[CustomHouse], tags=["CustomHouse"] )
def getCustomHouse():
    return conn.execute( customHouseModel.select() ).fetchall()

@customHouse.get( "/customHouse/{id}", response_model=CustomHouse, tags=["CustomHouse"] )
def getHouse( id: int ):
    return conn.execute( customHouseModel.select().where( customHouseModel.c.id == id ) ).first()

@customHouse.post( "/customHouse", response_model=CustomHouse, tags=["CustomHouse"] )
def createCustomHouse( customHouseSchema: CustomHouse ):
    result = conn.execute( customHouseModel.insert().values( customHouseSchema.dict() ) )
    return conn.execute( customHouseModel.select().where( customHouseModel.c.id == result.lastrowid ) ).first()

@customHouse.delete( "/customHouse/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["CustomHouse"] )
def deleteCustomHouse( id: int ):
    result = conn.execute( customHouseModel.delete().where( customHouseModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@customHouse.put( "/customHouse/{id}", response_model=CustomHouse, tags=["CustomHouse"] )
def updateCustomHouse( id: int, customHouseSchema: CustomHouse ):
    conn.execute( customHouseModel.update().values( customHouseSchema.dict() ).where( customHouseModel.c.id == id ) )
    return conn.execute( customHouseModel.select().where( customHouseModel.c.id == id ) ).first()
