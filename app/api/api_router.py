from fastapi import APIRouter

from app.api import aztecode, barcode, datamatrix, qrcode

api_router = APIRouter()

api_router.include_router(aztecode.router, prefix="/aztec", tags=["aztec"])
api_router.include_router(barcode.router, prefix="/barcode", tags=["barcode"])
api_router.include_router(datamatrix.router, prefix="/datamatrix", tags=["datamatrix"])
api_router.include_router(qrcode.router, prefix="/qrcode", tags=["qrcode"])
