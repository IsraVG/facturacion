from fastapi import APIRouter
from Config.db import conn
# from Models.coin import coin as coinModel
from Schemas.stamped import Stamped
# from starlette.status import HTTP_204_NO_CONTENT
from Services.CreationFiles.createXml import CreateXml
from ServiceSoap import ServiceSoap

service = APIRouter()

@service.post( "/timbrado", tags=["ServiceIntegrator"] )
def getStamped( schemaStamped: dict ):
    print( schemaStamped )
    CreateXml( schemaStamped, "timbrado.xml" )
    return SoapService( schemaStamped, "timbrado.xml", "timbrado" )

@service.post( "/complemento", tags=["ServiceIntegrator"] )
def getComplement( schemaComplement: dict ):
    print( schemaComplement )

@service.post( "/notacredito", tags=["ServiceIntegrator"] )
def getCreditNote( schemaCreditNote: dict ):
    CreateXml( schemaCreditNote, "notaCredito.xml" )
    return SoapService( schemaCreditNote, "notaCredito.xml", "timbrado" )

@service.post( "/cancelacion", tags=["ServiceIntegrator"] )
def getCancellation( schemaCancellation: dict ):
    print( schemaCancellation )
    data = { 
        "rfcEmisor" : schemaCancellation['rfcEmisor'],
        "folioUUID" : schemaCancellation['folioUUID'],
        "motivoCancelacion" : schemaCancellation['motivoCancelacion'],
        "folioUUIDSustitucion" : schemaCancellation['folioUUIDSustitucion'],
    }
    return SoapService( schemaCancellation, None, "cancelacion", data )

@service.post( "/statusSat", tags=["ServiceIntegrator"] )
def getStatusSat( schemaStatusSat: dict ):
    print( schemaStatusSat )
    data = { "folioUUID" : schemaStatusSat['folioUUID'] }
    return SoapService( schemaStatusSat, None, "statusSat", data )


def SoapService( schema, nameFile, event, data = None):
    try:
        # response = ServiceSoap.service( "https://pruebas.timbracfdi33.mx/Timbrado.asmx?wsdl", "mvpNUXmQfK8=" )
        # response = ServiceSoap.service( schema['URLServicioFacturacion'], schema['UsuarioIntegrador'], "xmlTimbrado.xml", "timbrado" )
        response = ServiceSoap.service( 
            schema['URLServicioFacturacion'], 
            schema['UsuarioIntegrador'],#"mvpNUXmQfK8=", 
            nameFile, 
            event,
            data
        )
    except Exception as e:
        print( e )
        response = e
    
    return response
