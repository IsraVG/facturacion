from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.typeFactor import typeFactor as factorModel
from Schemas.typeFactor import TypeFactor
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

typeFactor = APIRouter()

@typeFactor.get( "/typeFactor", response_model=List[TypeFactor], tags=["TypeFactor"] )
def getTypeFactor():
    return conn.execute( factorModel.select() ).fetchall()

@typeFactor.get( "/typeFactor/{id}", response_model=TypeFactor, tags=["TypeFactor"] )
def getFactor( id: int ):
    return conn.execute( factorModel.select().where( factorModel.c.id == id ) ).first()

@typeFactor.post( "/typeFactor", response_model=TypeFactor, tags=["TypeFactor"] )
def createTypeFactor( factorSchema: TypeFactor ):
    result = conn.execute( factorModel.insert().values( factorSchema.dict() ) )
    return conn.execute( factorModel.select().where( factorModel.c.id == result.lastrowid ) ).first()

@typeFactor.delete( "/typeFactor/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["TypeFactor"] )
def deleteTypeFactor( id: int ):
    result = conn.execute( factorModel.delete().where( factorModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@typeFactor.put( "/typeFactor/{id}", response_model=TypeFactor, tags=["TypeFactor"] )
def updateTypeFactor( id: int, factorSchema: TypeFactor ):
    conn.execute( factorModel.update().values( factorSchema.dict() ).where( factorModel.c.id == id ) )
    return conn.execute( factorModel.select().where( factorModel.c.id == id ) ).first()
