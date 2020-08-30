import barcode

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import FileResponse
from barcode.writer import ImageWriter

router = APIRouter()


class Barcode(BaseModel):
    barcode_type: str
    barcode_message: str


@router.post("/generate")
async def barcode_image(barcode_gen: Barcode):
    message_filename = "./barcode/" + barcode_gen.barcode_message

    ean = barcode.get(barcode_gen.barcode_type, barcode_gen.barcode_message, writer=ImageWriter())
    filename = ean.save(message_filename)
    return FileResponse(filename)
