from fastapi import APIRouter, Response, status
from Config.db import conn
from Models.relationshipTypes import relationshipTypes as relationshipModel
from Schemas.relationshipTypes import RelationshipTypes
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

relationshipTypes = APIRouter()

@relationshipTypes.get( "/relationshipTypes", response_model=List[RelationshipTypes], tags=["RelationshipTypes"] )
def getRelationshipTypes():
    return conn.execute( relationshipModel.select() ).fetchall()

@relationshipTypes.get( "/relationshipTypes/{id}", response_model=RelationshipTypes, tags=["RelationshipTypes"] )
def getRelationshipType( id: int ):
    return conn.execute( relationshipModel.select().where( relationshipModel.c.id == id ) ).first()

@relationshipTypes.post( "/relationshipTypes", response_model=RelationshipTypes, tags=["RelationshipTypes"] )
def createRelationshipTypes( relationshipSchema: RelationshipTypes ):
    result = conn.execute( relationshipModel.insert().values( relationshipSchema.dict() ) )
    return conn.execute( relationshipModel.select().where( relationshipModel.c.id == result.lastrowid ) ).first()

@relationshipTypes.delete( "/relationshipTypes/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["RelationshipTypes"] )
def deleteRelationshipTypes( id: int ):
    result = conn.execute( relationshipModel.delete().where( relationshipModel.c.id == id ) )
    return Response( status_code=HTTP_204_NO_CONTENT )

@relationshipTypes.put( "/relationshipTypes/{id}", response_model=RelationshipTypes, tags=["RelationshipTypes"] )
def updateRelationshipTypes( id: int, relationshipSchema: RelationshipTypes ):
    conn.execute( relationshipModel.update().values( relationshipSchema.dict() ).where( relationshipModel.c.id == id ) )
    return conn.execute( relationshipModel.select().where( relationshipModel.c.id == id ) ).first()
