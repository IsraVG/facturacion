from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.wayPayment import wayPayment as payment
from Schemas.wayPayment import WayPayment
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

wayPayment = APIRouter()

@wayPayment.get( "/waypayments", response_model=List[WayPayment], tags=["WayPayment"] )
def getPayments():
    return conn.execute( payment.select() ).fetchall()

@wayPayment.get( "/waypayments/{id}", response_model=WayPayment, tags=["WayPayment"] )
def getPayment( id: int ):
    return conn.execute( payment.select().where( payment.c.id == id ) ).first()

@wayPayment.post( "/waypayments", response_model=WayPayment, tags=["WayPayment"] )
def createPayment( waypayment: WayPayment ):
    result = conn.execute( payment.insert().values( waypayment.dict() ) )
    return conn.execute( payment.select().where( payment.c.id == result.lastrowid ) ).first()

@wayPayment.delete( "/waypayments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["WayPayment"] )
def deletePayment( id: int ):
    result = conn.execute( payment.delete().where( payment.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@wayPayment.put( "/waypayments/{id}", response_model=WayPayment, tags=["WayPayment"] )
def updatePayment( id: int, waypayment: WayPayment ):
    conn.execute( payment.update().values( waypayment.dict() ).where( payment.c.id == id ) )
    return conn.execute( payment.select().where( payment.c.id == id ) ).first()
