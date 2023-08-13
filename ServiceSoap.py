from sqlalchemy import null
from suds.client import Client
import os, random, base64
# from xml.etree import ElementTree

class ServiceSoap:

    @classmethod

    def service( self, serviceUrl: str, userIntegrator: str, nameFile: str, event: str, data = None ):
        path = os.path.dirname( __file__ )
        xmlFile = None

        if data is None:
            with open( os.path.join( path, "Files", nameFile ), "r" ) as f: xmlFile = f.read()
            xmlFile64 = base64.b64encode( xmlFile.encode() )

        clie = Client( serviceUrl )

        if event == "timbrado":
            response = Client.dict( clie.service.TimbraCFDI( userIntegrator, xmlFile64.decode(), random.randint( 5, 999999 ) ) )
        
        elif event == "timbradoRetencion":
            response = Client.dict( clie.service.TimbraRetencion( userIntegrator, xmlFile64.decode(), random.randint( 5, 999999 ) ) )

        elif event == "cancelacion":
            response = Client.dict( clie.service.CancelaCFDI40( userIntegrator, data["rfcEmisor"], data["folioUUID"], data["motivoCancelacion"], data["folioUUIDSustitucion"] ) )

        elif event == "cancelacionRetencion":
            response = Client.dict( clie.service.CancelaRetencion( userIntegrator, "rfcEmisor", "folioUUID" ) )

        elif event == "aceptaRechaza":
            response = Client.dict( clie.service.AceptaRechazaCFDI( userIntegrator, "rfcReceptor", "folioUUID", "accion" ) )
        
        elif event == "setTimbres":
            response = Client.dict( clie.service.AsignaTimbresEmisor( userIntegrator, "rfcEmisor", "int noTimbres" ) )
        
        elif event == "getTimbres":
            response = Client.dict( clie.service.ObtieneTimbresDisponibles( userIntegrator, "rfcEmisor" ) )
        
        elif event == "statusSat":
            response = Client.dict( clie.service.ConsultaEstatusSat( userIntegrator, data['folioUUID'] ) )
        
        elif event == "peticionesPendientes":
            response = Client.dict( clie.service.ConsultaPeticionesPendientesCFDI( userIntegrator, "rfcReceptor" ) )

        # if response["anyType"][0] == '0' and response["anyType"][1] is None:
        #     with open( os.path.join( path, "Files", "fileXml.xml" ), "w" ) as f: f.write( response["anyType"][2] )

        #     parse = ElementTree.parse( os.path.join( path, "Files", "fileXml.xml" ) )
        #     root = parse.getroot()
        #     print( root.attrib )

        #     with open( os.path.join( path, "Files", "codeqr.jpg" ), "wb" ) as f: f.write( base64.b64decode( response["anyType"][3] ) ) 
        
        print( response )

        return response