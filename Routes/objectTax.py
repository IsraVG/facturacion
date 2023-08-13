from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.objectTax import objectTax as objectTaxModel
from Schemas.objectTax import ObjectTax
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

objectTax = APIRouter()

@objectTax.get( "/objectTax", response_model=List[ObjectTax], tags=["ObjectTax"] )
def getObjectTax():
    return conn.execute( objectTaxModel.select() ).fetchall()

@objectTax.get( "/objectTax/{id}", response_model=ObjectTax, tags=["ObjectTax"] )
def getObject( id: int ):
    return conn.execute( objectTaxModel.select().where( objectTaxModel.c.id == id ) ).first()

@objectTax.post( "/objectTax", response_model=ObjectTax, tags=["ObjectTax"] )
def createObjectTax( objectTaxSchema: ObjectTax ):
    result = conn.execute( objectTaxModel.insert().values( objectTaxSchema.dict() ) )
    return conn.execute( objectTaxModel.select().where( objectTaxModel.c.id == result.lastrowid ) ).first()

@objectTax.delete( "/objectTax/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["ObjectTax"] )
def deleteObjectTax( id: int ):
    result = conn.execute( objectTaxModel.delete().where( objectTaxModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@objectTax.put( "/objectTax/{id}", response_model=ObjectTax, tags=["ObjectTax"] )
def updateObjectTax( id: int, objectTaxSchema: ObjectTax ):
    conn.execute( objectTaxModel.update().values( objectTaxSchema.dict() ).where( objectTaxModel.c.id == id ) )
    return conn.execute( objectTaxModel.select().where( objectTaxModel.c.id == id ) ).first()
