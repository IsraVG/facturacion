from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()

pdf.image( os.path.join( os.path.dirname(__file__), "..", "..", "Files", "casa-kame.jpg" ), 5, 5, 35, 15, "JPG")

pdf.set_font('Arial', 'B', 12)
pdf.set_text_color( 0, 88, 159 )

pdf.set_xy( 45, 5 )
pdf.cell( 40, 5, 'UNIVERSIDAD DEL PEDREGAL DEL SUR S.C' )

pdf.set_text_color( 0, 0, 0 )

pdf.set_xy( 45, 10 )
pdf.cell( 40, 5, 'UPS900305844' )

pdf.set_font('Arial', 'B', 10)

pdf.set_xy( 45, 15 )
pdf.cell( 40, 5, '601-General de Ley Personas Morales' )

pdf.set_fill_color( 238, 238, 238)

pdf.set_xy( 155, 5 )
pdf.cell( 50, 5, 'CFDI Version 4.0', 0, 1, 'L', True )

pdf.set_xy( 155, 10 )
pdf.cell( 50, 5, 'FOLIO FISCAL:', 0, 1, 'L', True )

pdf.set_font('Arial', '', 8)
pdf.set_xy( 155, 15 )
pdf.cell( 50, 5, '1faf5a4e-b673-4fec-b6f2-b97d3318e8fb')

pdf.set_xy( 155, 20 )
pdf.cell( 50, 5, '30001000000400002495')

pdf.set_font('Arial', 'B', 7)
pdf.set_xy( 155, 25 )
pdf.cell( 50, 5, 'Codigo Postal, Fecha y Hora de Emision', 0, 1, 'L', True)

pdf.set_xy( 155, 40 )
pdf.cell( 50, 5, 'Serie y Folio', 0, 1, 'L', True)

pdf.set_xy( 155, 30 )
pdf.cell( 50, 5, 'C.P: 14370')

pdf.set_xy( 155, 35 )
pdf.cell( 50, 5, '2022-03-04T10:25:38')

pdf.set_xy( 155, 45 )
pdf.cell( 50, 5, '89067-28476')

pdf.line( 5 , 28, 155, 28 )

pdf.set_font('Arial', 'B', 12)
pdf.set_text_color( 150, 150, 150 )

pdf.set_xy( 10, 30 )
pdf.cell( 35, 5, 'Cliente' )

pdf.set_font('Arial', 'B', 12)
pdf.set_text_color( 0, 88, 159 )

pdf.set_xy( 40, 35 )
pdf.cell( 40, 5, 'PUBLICO EN GENERAL' )

pdf.set_font('Arial', '', 12)
pdf.set_text_color( 0, 0, 0 )

pdf.set_xy( 40, 40 )
pdf.cell( 40, 5, 'XAXX010101000' )

pdf.set_font('Arial', '', 8)

pdf.set_xy( 40, 45 )
pdf.cell( 40, 5, 'P01 - Por Definir' )

pdf.set_fill_color( 238, 238, 238)

pdf.set_font('Arial', 'B', 8)
pdf.set_xy( 5, 55 )
pdf.cell( 17, 5, 'Clave SAT', 0, 1, 'L', True )

pdf.set_xy( 22, 55 )
pdf.cell( 13, 5, 'Codigo', 0, 1, 'L', True )

pdf.set_xy( 35, 55 )
pdf.cell( 15, 5, 'Cantidad', 0, 1, 'L', True )

pdf.set_xy( 50, 55 )
pdf.cell( 74, 5, 'Descripcion', 0, 1, 'L', True )

pdf.set_xy( 124, 55 )
pdf.cell( 25, 5, 'Precio Unitario', 0, 1, 'L', True )

pdf.set_xy( 149, 55 )
pdf.cell( 20, 5, 'Unidad SAT', 0, 1, 'L', True )

pdf.set_xy( 169, 55 )
pdf.cell( 18, 5, 'Unidad', 0, 1, 'L', True )

pdf.set_xy( 187, 55 )
pdf.cell( 18, 5, 'Importe', 0, 1, 'L', True )

pdf.set_font('Arial', '', 8)
pdf.set_xy( 5, 60 )
pdf.cell( 17, 10, '86121700', 0, 1, 'C' )

pdf.set_xy( 22, 60 )
pdf.cell( 13, 10, '18', 0, 1, 'C' )

pdf.set_xy( 35, 60 )
pdf.cell( 15, 10, '1', 0, 1, 'C' )

pdf.set_font('Arial', '', 6)
pdf.set_xy( 50, 60 )
pdf.multi_cell( 74, 3, 'LEÓN ALCÁNTARA ALONDRA CURP LEAA011109MDFNLLA8 CONTADURÍA PÚBLICA Y DIRECCIÓN FINANCIERA RVOE 922595 COLEGIATURA FEBRERO 2022', 0, 'L' )

pdf.set_font('Arial', '', 8)
pdf.set_xy( 124, 60 )
pdf.cell( 25, 10, '$ 7337.00', 0, 1, 'R' )

pdf.set_xy( 149, 60 )
pdf.cell( 20, 10, 'E48', 0, 1, 'C' )

pdf.set_xy( 169, 60 )
pdf.cell( 18, 10, 'NO APLICA', 0, 1, 'C' )

pdf.set_xy( 187, 60 )
pdf.cell( 18, 10, '$ 7337.00', 0, 1, 'R' )

pdf.line( 5 , 85, 205, 85 )

pdf.set_font('Arial', 'B', 10)
pdf.set_text_color( 150, 150, 150 )

pdf.set_xy( 5, 85 )
pdf.cell( 40, 5, 'Importe con letra:' )

pdf.set_text_color( 0, 0, 0 )

pdf.set_xy( 5, 90 )
pdf.cell( 60, 5, 'CIENTO CINCUENTA PESOS 00/100 M.N.' )

pdf.set_xy( 150, 85 )
pdf.cell( 30, 5, 'Subtotal' )

pdf.set_xy( 150, 90 )
pdf.cell( 30, 5, 'Descuento' )

pdf.set_xy( 150, 95 )
pdf.cell( 30, 5, 'IVA 0.00 %' )

pdf.set_xy( 150, 100 )
pdf.cell( 30, 5, 'TOTAL', 0, 1, 'L', True )

pdf.set_xy( 175, 85 )
pdf.cell( 30, 5, '$ 150.00', 0, 1, 'R' )

pdf.set_xy( 175, 90 )
pdf.cell( 30, 5, '$ 0.00', 0, 1, 'R' )

pdf.set_xy( 175, 95 )
pdf.cell( 30, 5, '$ 0.00', 0, 1, 'R' )

pdf.set_xy( 175, 100 )
pdf.cell( 30, 5, '$ 150.00', 0, 1, 'R', True )

pdf.set_xy( 5, 100 )
pdf.cell( 145, 5, '03 - TRANSFERENCIA | PUE - Pago en una sola exhibición', 0, 1, 'L', True )





pdf.set_xy( 5, 140 )
pdf.cell( 200, 5, 'Sello digital del CFDI:' )

pdf.set_xy( 5, 145 )
pdf.multi_cell( 200, 5, "cm43E1k06IFtu1k7BMFPYdKbhwBWj5WRLeOhQACF+b6VwMndpKefg4Z7xW/sofofEGjopGK1Hjv/IiekXO6/hIdpiwtawgUCq156R5ptjJIf5jAHPfoTnQNIyLSZDeSdKHTO20+pua0bcB24t7oUurT2PgoGgE6S02geaVLbTGVbEFtzMRqf37JbY9Zhz7rDdb+KuWOOLabSwf9Drb4tjHb0D8nNn0DeaKg9zLMQUN+GwbsXHbAzd1nNC5V9QCx/+J0nB/uiPUvHrEl8sfbpy/Q32vPi02e7kN36UItloHiOQHuHZ/fsGz8EqhmR95MlldBcMCjFI/2KlzYoZJ4lMg==", 0, 1, 'L' )

pdf.set_xy( 5, 170 )
pdf.cell( 200, 5, 'Sello del SAT:' )

pdf.set_xy( 5, 175 )
pdf.multi_cell( 200, 5, "wjLZQX8+SSeKl4poJkj/mO/MFWZkGjiDgvzxUNkH8Snnjy4DSrnVwxfXysnhs1z2wO87GAB34GtLY8hBCnkK9l8bcp4XQ7xtSsKPZdlVeeXMTvx4Yn5aL3MXe6iXUs4ZXVnBYGuAsljbGB1xs+OAzJV0hbY7B9hiwI9FSArG9Xea5XXLTeai2lO95RIkyIT25TcR2athZX7zic5qJtNz8OlsHhpIRtfQxojEDCVNa/yv8TNSUkqcrEH0+AgMVRcH+tiJCk+O1vZCjbGK6V9zP0ic5PX3SSLvAZfiEQxyhHP40VmRhDthT1peEsMr9/IS0wKDA2/UcFUkwACa3ByZ1g==", 0, 1, 'L' )

pdf.set_xy( 5, 200 )
pdf.cell( 200, 5, 'Cadena original del complemento de certificación digital del SAT:' )

pdf.set_xy( 5, 205 )
pdf.multi_cell( 200, 5, "||1.1|3097d879-e837-4e62-89af-4937b8c564c5|2021-07-30T09:59:14|LSO1306189R5|cm43E1k06IFtu1k7BMFPYdKbhwBWj5WRLeOhQACF+b6VwMndpKefg4Z7xW/sofofEGjopGK1Hjv/IiekXO6/hIdpiwtawgUCq156R5ptjJIf5jAHPfoTnQNIyLSZDeSdKHTO20+pua0bcB24t7oUurT2PgoGgE6S02geaVLbTGVbEFtzMRqf37JbY9Zhz7rDdb+KuWOOLabSwf9Drb4tjHb0D8nNn0DeaKg9zLMQUN+GwbsXHbAzd1nNC5V9QCx/+J0nB/uiPUvHrEl8sfbpy/Q32vPi02e7kN36UItloHiOQHuHZ/fsGz8EqhmR95MlldBcMCjFI/2KlzYoZJ4lMg==|00001000000408254801||", 0, 1, 'L' )

pdf.set_xy( 5, 240 )
pdf.cell( 100, 5, 'No de Serie de Certificado del SAT:' )

pdf.set_xy( 5, 245 )
pdf.cell( 100, 5, '00001000000408254801' )


pdf.set_xy( 5, 250 )
pdf.cell( 100, 5, 'Fecha y hora de certificacion:' )

pdf.set_xy( 5, 255 )
pdf.cell( 100, 5, '2021-07-30T09:59:14' )

pdf.set_xy( 5, 270 )
pdf.cell( 200, 5, 'Este documento es una representacion impresa de un CFDI', 0, 1, 'C', True )

pdf.output( os.path.join( os.path.dirname(__file__), "..", "..", "Files", "pdfTimbrado.pdf" ) )