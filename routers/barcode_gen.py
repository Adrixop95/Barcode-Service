from io import BytesIO

from fastapi import APIRouter, File
from pydantic import BaseModel, Field
from starlette.responses import FileResponse
from pyzbar.pyzbar import decode
from PIL import Image

from barcode.writer import ImageWriter
import barcode


router = APIRouter()


class Barcode(BaseModel):
    barcode_type: str = Field(..., title="Barcode type")
    barcode_message: str = Field(..., title="Barcode message")


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
