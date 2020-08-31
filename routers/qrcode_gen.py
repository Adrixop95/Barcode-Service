import pyqrcode

from fastapi import APIRouter, File
from pydantic import BaseModel, Field
from starlette.responses import FileResponse
from pyzbar.pyzbar import decode
from io import BytesIO
from PIL import Image

router = APIRouter()


class QRCode(BaseModel):
    qrcode_scale: int = Field(..., title="QRCode scale")
    qrcode_message: str = Field(..., title="QRCode message")
    qrcode_error_correct: str = Field(None, title="QRCode error correct")


@router.post("/generate")
async def qrcode_image_generate(qrcode_gen: QRCode):
    message_filename = "./qrcode/" + qrcode_gen.qrcode_message.replace('/', '') + ".png"

    if qrcode_gen.qrcode_error_correct is not None:
        url = pyqrcode.create(qrcode_gen.qrcode_message, qrcode_gen.qrcode_error_correct)
        print(url)
    else:
        url = pyqrcode.create(qrcode_gen.qrcode_message)
        print(url)

    url.png(message_filename, qrcode_gen.qrcode_scale)
    return FileResponse(message_filename)


@router.post("/decrypt")
async def qrcode_image_decrypt(file: bytes = File(...)):
    stream = BytesIO(file)
    img = Image.open(stream)

    return decode(img)
