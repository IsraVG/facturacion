from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.voucherType import voucherType
from Schemas.voucherType import VoucherType
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

voucher = APIRouter()

@voucher.get( "/vouchertype", response_model=List[VoucherType], tags=["VoucherType"] )
def getVouchers():
    return conn.execute( voucherType.select() ).fetchall()

@voucher.get( "/vouchertype/{id}", response_model=VoucherType, tags=["VoucherType"] )
def getVoucher( id: int ):
    return conn.execute( voucherType.select().where( voucherType.c.id == id ) ).first()

@voucher.post( "/vouchertype", response_model=VoucherType, tags=["VoucherType"] )
def createVoucher( typevoucher: VoucherType ):
    result = conn.execute( voucherType.insert().values( typevoucher.dict() ) )
    return conn.execute( voucherType.select().where( voucherType.c.id == result.lastrowid ) ).firstvoucher

@voucher.delete( "/vouchertype/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["VoucherType"] )
def deleteVoucher( id: int ):
    result = conn.execute( voucherType.delete().where( voucherType.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@voucher.put( "/vouchertype/{id}", response_model=VoucherType, tags=["VoucherType"] )
def updateVoucher( id: int, typevoucher: VoucherType ):
    conn.execute( voucherType.update().values( typevoucher.dict() ).where( voucherType.c.id == id ) )
    return conn.execute( voucherType.select().where( voucherType.c.id == id ) ).first()
