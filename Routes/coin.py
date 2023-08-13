from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.coin import coin as coinModel
from Schemas.coin import Coin
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

coin = APIRouter()

@coin.get( "/coins", response_model=List[Coin], tags=["Coin"] )
def getCoins():
    return conn.execute( coinModel.select() ).fetchall()

@coin.get( "/coins/{id}", response_model=Coin, tags=["Coin"] )
def getCoin( id: int ):
    return conn.execute( coinModel.select().where( coinModel.c.id == id ) ).first()

@coin.post( "/coins", response_model=Coin, tags=["Coin"] )
def createCoin( coinSchema: Coin ):
    result = conn.execute( coinModel.insert().values( coinSchema.dict() ) )
    return conn.execute( coinModel.select().where( coinModel.c.id == result.lastrowid ) ).first()

@coin.delete( "/coins/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Coin"] )
def deleteCoin( id: int ):
    result = conn.execute( coinModel.delete().where( coinModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@coin.put( "/coins/{id}", response_model=Coin, tags=["Coin"] )
def updateCoin( id: int, coinSchema: Coin ):
    conn.execute( coinModel.update().values( coinSchema.dict() ).where( coinModel.c.id == id ) )
    return conn.execute( coinModel.select().where( coinModel.c.id == id ) ).first()
