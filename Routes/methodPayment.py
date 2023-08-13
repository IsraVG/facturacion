from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.methodPayment import methodPayment as paymentMethod
from Schemas.methodPayment import MethodPayment
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

methodPayment = APIRouter()

@methodPayment.get( "/methodPayment", response_model=List[MethodPayment], tags=["MethodPayment"] )
def getMethodPayments():
    return conn.execute( paymentMethod.select() ).fetchall()

@methodPayment.get( "/methodPayment/{id}", response_model=MethodPayment, tags=["MethodPayment"] )
def getMethodPayment( id: int ):
    return conn.execute( paymentMethod.select().where( paymentMethod.c.id == id ) ).first()

@methodPayment.post( "/methodPayment", response_model=MethodPayment, tags=["MethodPayment"] )
def createMethodPayment( methodSchema: MethodPayment ):
    result = conn.execute( paymentMethod.insert().values( methodSchema.dict() ) )
    return conn.execute( paymentMethod.select().where( paymentMethod.c.id == result.lastrowid ) ).first()

@methodPayment.delete( "/methodPayment/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["MethodPayment"] )
def deleteMethodPayment( id: int ):
    result = conn.execute( paymentMethod.delete().where( paymentMethod.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@methodPayment.put( "/methodPayment/{id}", response_model=MethodPayment, tags=["MethodPayment"] )
def updateMethodPayment( id: int, methodSchema: MethodPayment ):
    conn.execute( paymentMethod.update().values( methodSchema.dict() ).where( paymentMethod.c.id == id ) )
    return conn.execute( paymentMethod.select().where( paymentMethod.c.id == id ) ).first()
