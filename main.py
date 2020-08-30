import pyqrcode
import barcode
import os

from aztec_code_generator import AztecCode
from barcode.writer import ImageWriter
from pydantic import BaseModel
from starlette.responses import FileResponse
from pylibdmtx.pylibdmtx import encode
from PIL import Image
from typing import Optional

from fastapi import FastAPI


class Barcode(BaseModel):
    barcode_type: str
    barcode_message: str


class QRCode(BaseModel):
    qrcode_scale: int
    qrcode_message: str
    qrcode_error_correct: Optional[str] = None


class Aztec(BaseModel):
    aztec_code_scale: int
    aztec_code_message: str


class DataMatrix(BaseModel):
    data_matrix_message: str


app = FastAPI()


@app.on_event("startup")
async def create_folder_structure():
    folders = ['./barcode', './qrcode', './aztec', './datamatrix']
    try:
        for folder in folders:
            os.mkdir(os.path.join(folder))
    except OSError:
        return


@app.get("/")
async def root():
    return {"Greetings": "Hey! Thank you for using this service. If you don't know how to use it, check out readme on "
                         "Github.",
            "Repository": "https://github.com/Adrixop95/BarcodeGenerator/",
            "MOTD": "Have a nice day : D"
            }


@app.post("/barcode")
async def barcode_image(barcode_gen: Barcode):
    message_filename = "./barcode/" + barcode_gen.barcode_message

    ean = barcode.get(barcode_gen.barcode_type, barcode_gen.barcode_message, writer=ImageWriter())
    filename = ean.save(message_filename)
    return FileResponse(filename)


@app.post("/qrcode")
async def qrcode_image(qrcode_gen: QRCode):
    message_filename = "./qrcode/" + qrcode_gen.qrcode_message.replace('/', '') + ".png"

    if qrcode_gen.qrcode_error_correct is not None:
        url = pyqrcode.create(qrcode_gen.qrcode_message, qrcode_gen.qrcode_error_correct)
        print(url)
    else:
        url = pyqrcode.create(qrcode_gen.qrcode_message)
        print(url)

    url.png(message_filename, qrcode_gen.qrcode_scale)
    return FileResponse(message_filename)


@app.post("/aztec")
async def aztec_code_image(aztec_gen: Aztec):
    message_filename = "./aztec/" + aztec_gen.aztec_code_message.replace('/', '') + ".png"

    aztec_code = AztecCode(message_filename)
    aztec_code.save(message_filename, aztec_gen.aztec_code_scale)
    return FileResponse(message_filename)


@app.post("/datamatrix")
async def data_matrix_image(data_gen: DataMatrix):
    message_filename = "./datamatrix/" + data_gen.data_matrix_message.replace('/', '') + ".png"

    encoded = encode(data_gen.data_matrix_message.encode('utf8'))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save(message_filename)
    return FileResponse(message_filename)
