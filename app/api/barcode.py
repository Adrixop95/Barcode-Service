from io import BytesIO

import barcode
from PIL import Image
from barcode.writer import ImageWriter
from fastapi import APIRouter, File
from pyzbar.pyzbar import decode
from starlette.responses import FileResponse

from app.schemes.barcode import Barcode

router = APIRouter()


@router.post("/generate")
async def barcode_image(barcode_gen: Barcode):
    message_filename = "./barcode/" + barcode_gen.barcode_message

    ean = barcode.get(barcode_gen.barcode_type, barcode_gen.barcode_message, writer=ImageWriter())
    filename = ean.save(message_filename)
    return FileResponse(filename)


@router.post("/decrypt")
async def barcode_decrypt(file: bytes = File(...)):
    stream = BytesIO(file)
    img = Image.open(stream)

    return decode(img)
