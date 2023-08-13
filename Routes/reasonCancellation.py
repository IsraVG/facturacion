from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.reasonCancellation import reasonCancellation as reasonCancellationModel
from Schemas.reasonCancellation import ReasonCancellation
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

reasonCancel = APIRouter()

@reasonCancel.get( "/reasonCancel", response_model=List[ReasonCancellation], tags=["ReasonCancel"] )
def getReasonCancel():
    return conn.execute( reasonCancellationModel.select() ).fetchall()

@reasonCancel.get( "/reasonCancel/{id}", response_model=ReasonCancellation, tags=["ReasonCancel"] )
def getReason( id: int ):
    return conn.execute( reasonCancellationModel.select().where( reasonCancellationModel.c.id == id ) ).first()

@reasonCancel.post( "/reasonCancel", response_model=ReasonCancellation, tags=["ReasonCancel"] )
def createReasonCancel( ReasonCancelSchema: ReasonCancellation ):
    result = conn.execute( reasonCancellationModel.insert().values( ReasonCancelSchema.dict() ) )
    return conn.execute( reasonCancellationModel.select().where( reasonCancellationModel.c.id == result.lastrowid ) ).first()

@reasonCancel.delete( "/reasonCancel/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["ReasonCancel"] )
def deleteReasonCancel( id: int ):
    result = conn.execute( reasonCancellationModel.delete().where( reasonCancellationModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@reasonCancel.put( "/reasonCancel/{id}", response_model=ReasonCancellation, tags=["ReasonCancel"] )
def updateReasonCancel( id: int, ReasonCancelSchema: ReasonCancellation ):
    conn.execute( reasonCancellationModel.update().values( ReasonCancelSchema.dict() ).where( reasonCancellationModel.c.id == id ) )
    return conn.execute( reasonCancellationModel.select().where( reasonCancellationModel.c.id == id ) ).first()
