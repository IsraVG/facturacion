from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.periodicity import periodicity as periodicityModel
from Schemas.periodicity import Periodicity
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

periodicity = APIRouter()

@periodicity.get( "/periodicity", response_model=List[Periodicity], tags=["Periodicity"] )
def getPeriodicity():
    return conn.execute( periodicityModel.select() ).fetchall()

@periodicity.get( "/periodicity/{id}", response_model=Periodicity, tags=["Periodicity"] )
def getPeri( id: int ):
    return conn.execute( periodicityModel.select().where( periodicityModel.c.id == id ) ).first()

@periodicity.post( "/periodicity", response_model=Periodicity, tags=["Periodicity"] )
def createPeriodicity( periodicitySchema: Periodicity ):
    result = conn.execute( periodicityModel.insert().values( periodicitySchema.dict() ) )
    return conn.execute( periodicityModel.select().where( periodicityModel.c.id == result.lastrowid ) ).first()

@periodicity.delete( "/periodicity/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Periodicity"] )
def deletePeriodicity( id: int ):
    result = conn.execute( periodicityModel.delete().where( periodicityModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@periodicity.put( "/periodicity/{id}", response_model=Periodicity, tags=["Periodicity"] )
def updatePeriodicity( id: int, periodicitySchema: Periodicity ):
    conn.execute( periodicityModel.update().values( periodicitySchema.dict() ).where( periodicityModel.c.id == id ) )
    return conn.execute( periodicityModel.select().where( periodicityModel.c.id == id ) ).first()
