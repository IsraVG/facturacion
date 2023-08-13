from xml.dom import minidom
import os

class CreateXml:

    doc = None
    xml = None
    data = None

    def __init__( self, data, nameFile ) -> None:
        self.data = data
        self.schema = "http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd"
        self.doc = minidom.Document()
        self.voucher()
        self.globalInformation()
        if "TipoRelacion" in self.data: 
            self.relationship()
        self.transmitter()
        self.receiver()
        self.concepts()
        if float( self.data["SubTotal"] ) != float( self.data["Total"] ):
            self.taxes()
        if self.data["TipoDeComprobante"] == "P":
            self.payments()
            #self.taxesPayment()

        xml_str = self.doc.toprettyxml( encoding="utf-8", indent="\t" )
        savePath = os.path.join( os.path.dirname(__file__), "..", "..", "Files", nameFile )

        with open( savePath, "wb" ) as f:
            f.write( xml_str )

    def voucher( self ) -> None: 
        self.xml = self.doc.createElement( "cfdi:Comprobante" )

        if self.data["TipoDeComprobante"] == "P": 
            self.schema += "http://www.sat.gob.mx/Pagos20 http://www.sat.gob.mx/sitio_internet/cfd/Pagos/Pagos20.xsd"
            self.xml.setAttribute( "xmlns:pago20", "http://www.sat.gob.mx/Pagos20" )

        self.xml.setAttribute( "xsi:schemaLocation", self.schema )
        self.xml.setAttribute( "xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance" )

        self.xml.setAttribute( "xmlns:cfdi", "http://www.sat.gob.mx/cfd/4" )

        #if self.data["TipoDeComprobante"] == "P": 
             

        self.xml.setAttribute( "Version", "4.0" )
        self.xml.setAttribute( "Serie", self.data["Serie"] )
        self.xml.setAttribute( "Folio", self.data["Folio"] )
        self.xml.setAttribute( "Fecha", self.data["Fecha"] )
        self.xml.setAttribute( "LugarExpedicion", self.data["LugarExpedicion"] )
        self.xml.setAttribute( "TipoDeComprobante", self.data["TipoDeComprobante"] )

        self.xml.setAttribute( "SubTotal", self.data["SubTotal"] ) # Este campo tiene que ser 0 si el tipo de comprobante es P
        self.xml.setAttribute( "Total", self.data["Total"] ) # Este campo tiene que ser 0 si el tipo de comprobante es P
        self.xml.setAttribute( "Moneda", self.data["Moneda"] ) # Este campo tiene que ser XXX si el tipo de comprobante es P
        self.xml.setAttribute( "Exportacion", self.data["Exportacion"] ) # Este campo tiene que ser 01 si el tipo de comprobante es P

        if self.data["TipoDeComprobante"] != "P": 
            if "InformacionGlobal" not in self.data:
                self.xml.setAttribute( "CondicionesDePago", "Efectivo" )
            self.xml.setAttribute( "FormaPago", self.data["FormaPago"] )
            self.xml.setAttribute( "MetodoPago", self.data["MetodoPago"] )
            self.xml.setAttribute( "Descuento", self.data["Descuento"] )

        self.doc.appendChild( self.xml )
    
    def globalInformation( self ) -> None:
        if "InformacionGlobal" in self.data:
            information = self.doc.createElement( 'cfdi:InformacionGlobal' )
            information.setAttribute( "Periodicidad", self.data["InformacionGlobal"]["Periodicidad"] )
            information.setAttribute( "Meses", self.data["InformacionGlobal"]["Mes"] )
            information.setAttribute( "Año", self.data["InformacionGlobal"]["Año"] )
            self.xml.appendChild( information )

    def relationship( self ) -> None:
        related = self.doc.createElement( 'cfdi:CfdiRelacionados' )
        related.setAttribute( "TipoRelacion", self.data["TipoRelacion"] )
        self.xml.appendChild( related )

        relation = self.doc.createElement( 'cfdi:CfdiRelacionado' )
        relation.setAttribute( "UUID", self.data["UUID"] )
        related.appendChild( relation )

    def transmitter( self ) -> None:
        Emisor = self.doc.createElement( 'cfdi:Emisor' )
        Emisor.setAttribute( "Rfc", self.data["Emisor"]["Rfc"] )
        Emisor.setAttribute( "Nombre", self.data["Emisor"]["Nombre"] )
        Emisor.setAttribute( "RegimenFiscal", self.data["Emisor"]["RegimenFiscal"] )
        self.xml.appendChild( Emisor )

    def receiver( self ) -> None:
        Receptor = self.doc.createElement( 'cfdi:Receptor' )
        Receptor.setAttribute( "Rfc", self.data["Receptor"]["Rfc"] )
        Receptor.setAttribute( "Nombre", self.data["Receptor"]["Nombre"] )
        Receptor.setAttribute( "RegimenFiscalReceptor", self.data["Receptor"]["RegimenFiscalReceptor"] )
        Receptor.setAttribute( "DomicilioFiscalReceptor", self.data["Receptor"]["DomicilioFiscalReceptor"] )
        Receptor.setAttribute( "UsoCFDI", self.data["Receptor"]["UsoCFDI"] )
        self.xml.appendChild( Receptor )

    def concepts( self ) -> None:
        Conceptos = self.doc.createElement( 'cfdi:Conceptos' )
        self.xml.appendChild( Conceptos )
        for concepto in self.data["Conceptos"]:
            Concepto = self.doc.createElement( 'cfdi:Concepto' )
            Concepto.setAttribute( "ClaveProdServ", concepto["ClaveProdServ"] ) # Este campo debe ser "84111506" si es P
            #Concepto.setAttribute( "NoIdentificacion", concepto["NoIdentificacion"] )
            Concepto.setAttribute( "Cantidad", concepto["Cantidad"] ) # Este campo debe ser 1 si es P
            Concepto.setAttribute( "ClaveUnidad", concepto["ClaveUnidad"] ) # Este campo debe ser "ACT" si es P
            Concepto.setAttribute( "Descripcion", concepto["Descripcion"] ) # Este campo debe ser "Pago" si es P
            Concepto.setAttribute( "ValorUnitario", concepto["ValorUnitario"] ) # Este campo debe ser 0 si es P
            Concepto.setAttribute( "Importe", concepto["Importe"] ) # Este campo debe ser 0 si es P
            Concepto.setAttribute( "ObjetoImp", concepto["ObjetoImp"] ) # Este campo debe ser "01" si es P

            if self.data["TipoDeComprobante"] != "P":
                Concepto.setAttribute( "Unidad", concepto["Unidad"] )
                Concepto.setAttribute( "Descuento", concepto["Descuento"] )
                Concepto.setAttribute( "NoIdentificacion", concepto["NoIdentificacion"] )
    
            Conceptos.appendChild( Concepto )

            if concepto["ObjetoImp"] == "02":
                Impuestos = self.doc.createElement( 'cfdi:Impuestos' )
                Concepto.appendChild( Impuestos )

                Traslados = self.doc.createElement( 'cfdi:Traslados' )
                Impuestos.appendChild( Traslados )

                Traslado = self.doc.createElement( 'cfdi:Traslado' )
                Traslado.setAttribute( "Base", str( concepto["Traslado"]["Base"] ) )
                Traslado.setAttribute( "Importe", str( concepto["Traslado"]["Importe"] ) )
                Traslado.setAttribute( "Impuesto", str( concepto["Traslado"]["Impuesto"] ) )
                Traslado.setAttribute( "TasaOCuota", str( concepto["Traslado"]["TasaOCuota"] ) )
                Traslado.setAttribute( "TipoFactor", concepto["Traslado"]["TipoFactor"] )
                Traslados.appendChild( Traslado )

                """ Retenciones = self.doc.createElement( 'cfdi:Retenciones' )
                Impuestos.appendChild( Retenciones )

                Retencion = self.doc.createElement( 'cfdi:Retencion' )
                Retencion.setAttribute( "Base", "1" )
                Retencion.setAttribute( "Importe", "0.00" )
                Retencion.setAttribute( "Impuesto", "001" )
                Retencion.setAttribute( "TasaOCuota", "0.100000" )
                Retencion.setAttribute( "TipoFactor", "Tasa" )
                Retenciones.appendChild( Retencion ) """

    def taxes( self ) -> None:
        Impuestos = self.doc.createElement( 'cfdi:Impuestos' )
        #Impuestos.setAttribute( "TotalImpuestosRetenidos", "0.00" )
        Impuestos.setAttribute( "TotalImpuestosTrasladados", self.data["Traslados"]["TotalImpuestosTrasladados"] )
        self.xml.appendChild( Impuestos )

        """ etenciones = self.doc.createElement( 'cfdi:Retenciones' )
        Impuestos.appendChild( Retenciones )

        Retencion = self.doc.createElement( 'cfdi:Retencion' )
        Retencion.setAttribute( "Importe", "0.00" )
        Retencion.setAttribute( "Impuesto", "001" )
        Retenciones.appendChild( Retencion )

        Retencion = self.doc.createElement( 'cfdi:Retencion' )
        Retencion.setAttribute( "Importe", "0.00" )
        Retencion.setAttribute( "Impuesto", "002" )
        Retenciones.appendChild( Retencion ) """

        Traslados = self.doc.createElement( 'cfdi:Traslados' )
        Impuestos.appendChild( Traslados )

        Traslado = self.doc.createElement( 'cfdi:Traslado' )
        Traslado.setAttribute( "Base", self.data["Traslados"]["Base"] )
        Traslado.setAttribute( "Importe", self.data["Traslados"]["Importe"] )
        Traslado.setAttribute( "Impuesto", self.data["Traslados"]["Impuesto"] )
        Traslado.setAttribute( "TasaOCuota", self.data["Traslados"]["TasaOCuota"] )
        Traslado.setAttribute( "TipoFactor", self.data["Traslados"]["TipoFactor"] )
        Traslados.appendChild( Traslado )

    def payments( self ) -> None:
        Complemento =  self.doc.createElement( 'cfdi:Complemento' )
        self.xml.appendChild( Complemento )

        Pagos = self.doc.createElement( 'pago20:Pagos' )
        Pagos.setAttribute( "Version", "2.0" )
        Complemento.appendChild( Pagos )

        Totales = self.doc.createElement( 'pago20:Totales' )
        Totales.setAttribute( "MontoTotalPagos", self.data["Totales"]['MontoTotalPagos'] )
        Pagos.appendChild( Totales )

        Pago = self.doc.createElement( 'pago20:Pago' )
        Pago.setAttribute( "FechaPago", self.data["Pagos"]['FechaPago'] )
        Pago.setAttribute( "FormaDePagoP", self.data["Pagos"]['FormaDePagoP'] )
        Pago.setAttribute( "MonedaP", self.data["Pagos"]['MonedaP'] )
        Pago.setAttribute( "Monto", self.data["Pagos"]['Monto'] )
         
        if "RfcEmisorCtaOrd" in self.data["Pagos"]:
            Pago.setAttribute( "RfcEmisorCtaOrd", self.data["Pagos"]['RfcEmisorCtaOrd'] )
        
        if "CtaOrdenante" in self.data["Pagos"]:
            Pago.setAttribute( "CtaOrdenante", self.data["Pagos"]['CtaOrdenante'] )

        if "RfcEmisorCtaBen" in self.data["Pagos"]:
            Pago.setAttribute( "RfcEmisorCtaBen", self.data["Pagos"]['RfcEmisorCtaBen'] )

        if "CtaBeneficiario" in self.data["Pagos"]:
            Pago.setAttribute( "CtaBeneficiario", self.data["Pagos"]['CtaBeneficiario'] )

        Pago.setAttribute( "TipoCambioP", "1" )
        Pagos.appendChild( Pago )

        for docRel in self.data["DocumentosRelacionados"]:
            DoctoRelacionado = self.doc.createElement( 'pago20:DoctoRelacionado' )
            DoctoRelacionado.setAttribute( "IdDocumento", docRel['IdDocumento'] )
            DoctoRelacionado.setAttribute( "MonedaDR", docRel['MonedaDR'] )
            DoctoRelacionado.setAttribute( "NumParcialidad", docRel['NumParcialidad'] )
            DoctoRelacionado.setAttribute( "ImpSaldoAnt", docRel['ImpSaldoAnt'] )
            DoctoRelacionado.setAttribute( "ImpPagado", docRel['ImpPagado'] )
            DoctoRelacionado.setAttribute( "ImpSaldoInsoluto", docRel['ImpSaldoInsoluto'] )
            DoctoRelacionado.setAttribute( "ObjetoImpDR", docRel['ObjetoImpDR'] )
            DoctoRelacionado.setAttribute( "EquivalenciaDR", "1" )
            Pago.appendChild( DoctoRelacionado )
    
    def taxesPayment( self ) -> None:
        Impuestos = self.doc.createElement( 'cfdi:Impuestos' )
        Impuestos.setAttribute( "TotalImpuestosRetenidos", "0.00" )
        Impuestos.setAttribute( "TotalImpuestosTrasladados", "0.16" )
        self.xml.appendChild( Impuestos )

        Retenciones = self.doc.createElement( 'cfdi:Retenciones' )
        Impuestos.appendChild( Retenciones )

        Retencion = self.doc.createElement( 'cfdi:Retencion' )
        Retencion.setAttribute( "Importe", "0.00" )
        Retencion.setAttribute( "Impuesto", "001" )
        Retenciones.appendChild( Retencion )

        Retencion = self.doc.createElement( 'cfdi:Retencion' )
        Retencion.setAttribute( "Importe", "0.00" )
        Retencion.setAttribute( "Impuesto", "002" )
        Retenciones.appendChild( Retencion )

        Traslados = self.doc.createElement( 'cfdi:Traslados' )
        Impuestos.appendChild( Traslados )

        Traslado = self.doc.createElement( 'cfdi:Traslado' )
        Traslado.setAttribute( "Base", "1" )
        Traslado.setAttribute( "Importe", "0.16" )
        Traslado.setAttribute( "Impuesto", "002" )
        Traslado.setAttribute( "TasaOCuota", "0.160000" )
        Traslado.setAttribute( "TipoFactor", "Tasa" )
        Traslados.appendChild( Traslado )
