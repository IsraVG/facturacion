from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.cfdiUse import useCfdi
from Schemas.cfdiUse import CfdiUse
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

cfdiUse = APIRouter()

@cfdiUse.get( "/cfdiUse", response_model=List[CfdiUse], tags=["CfdiUse"] )
def getCfdiUse():
    return conn.execute( useCfdi.select().order_by( useCfdi.c.code ) ).fetchall()

@cfdiUse.get( "/cfdiUse/{id}", response_model=CfdiUse, tags=["CfdiUse"] )
def getCfdi( id: int ):
    return conn.execute( useCfdi.select().where( useCfdi.c.id == id ) ).first()

@cfdiUse.post( "/cfdiUse", response_model=CfdiUse, tags=["CfdiUse"] )
def createCfdiUse( cfdiUseSchema: CfdiUse ):
    result = conn.execute( useCfdi.insert().values( cfdiUseSchema.dict() ) )
    return conn.execute( useCfdi.select().where( useCfdi.c.id == result.lastrowid ) ).first()

@cfdiUse.delete( "/cfdiUse/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["CfdiUse"] )
def deleteCfdiUse( id: int ):
    result = conn.execute( useCfdi.delete().where( useCfdi.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@cfdiUse.put( "/cfdiUse/{id}", response_model=CfdiUse, tags=["CfdiUse"] )
def updateCfdiUse( id: int, cfdiUseSchema: CfdiUse ):
    conn.execute( useCfdi.update().values( cfdiUseSchema.dict() ).where( useCfdi.c.id == id ) )
    return conn.execute( useCfdi.select().where( useCfdi.c.id == id ) ).first()
