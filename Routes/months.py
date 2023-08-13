from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.months import months as monthsModel
from Schemas.months import Months
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

months = APIRouter()

@months.get( "/months", response_model=List[Months], tags=["Months"] )
def getMonths():
    return conn.execute( monthsModel.select() ).fetchall()

@months.get( "/months/{id}", response_model=Months, tags=["Months"] )
def getMonth( id: int ):
    return conn.execute( monthsModel.select().where( monthsModel.c.id == id ) ).first()

@months.post( "/months", response_model=Months, tags=["Months"] )
def createMonth( monthsSchema: Months ):
    result = conn.execute( monthsModel.insert().values( monthsSchema.dict() ) )
    return conn.execute( monthsModel.select().where( monthsModel.c.id == result.lastrowid ) ).first()

@months.delete( "/months/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Months"] )
def deleteMonth( id: int ):
    result = conn.execute( monthsModel.delete().where( monthsModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@months.put( "/months/{id}", response_model=Months, tags=["Months"] )
def updateMonth( id: int, monthsSchema: Months ):
    conn.execute( monthsModel.update().values( monthsSchema.dict() ).where( monthsModel.c.id == id ) )
    return conn.execute( monthsModel.select().where( monthsModel.c.id == id ) ).first()
