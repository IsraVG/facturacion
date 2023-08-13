from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes.keyProductServices import keyProductServices
from Routes.relationshipTypes import relationshipTypes
from Routes.methodPayment import methodPayment
from Routes.customHouse import customHouse
from Routes.expedition import expedition
from Routes.wayPayment import wayPayment
from Routes.typeFactor import typeFactor
from Routes.voucherType import voucher
from Routes.taxRegime import taxRegime
from Routes.objectTax import objectTax
from Routes.taxation import taxation
from Routes.cfdiUse import cfdiUse
from Routes.unitKey import unitKey
from Routes.months import months
from Routes.coin import coin
from Routes.periodicity import periodicity

from Routes.reasonCancellation import reasonCancel

from Routes.serviceIntegrator import service

app = FastAPI(
    title="Api Facturacion",
    version="1.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router( keyProductServices )
app.include_router( relationshipTypes )
app.include_router( methodPayment )
app.include_router( customHouse )
app.include_router( expedition )
app.include_router( wayPayment )
app.include_router( typeFactor )
app.include_router( taxRegime )
app.include_router( objectTax )
app.include_router( taxation )
app.include_router( voucher )
app.include_router( cfdiUse )
app.include_router( unitKey )
app.include_router( months )
app.include_router( coin )
app.include_router( periodicity )

app.include_router( reasonCancel )

app.include_router( service )
