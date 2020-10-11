import shutil
import os

from aztec_code_generator import AztecCode
from fastapi import APIRouter, UploadFile, File
from starlette.responses import FileResponse

import zxing

from app.schemes.aztecode import Aztec


router = APIRouter()

reader = zxing.BarCodeReader()


@router.post("/generate")
async def aztec_code_image(aztec_gen: Aztec):
    message_filename = "./aztec/" + aztec_gen.aztec_code_message.replace('/', '').split(' ', 1)[0] + ".png"

    aztec_code = AztecCode(aztec_gen.aztec_code_message)
    aztec_code.save(message_filename, aztec_gen.aztec_code_scale)
    return FileResponse(message_filename)


@router.post("/decrypt")
async def aztec_code_decrypt(file: UploadFile = File(...)):

    upload_folder = "./aztec/upload/"
    file_object = file.file
    upload_folder = open(os.path.join(upload_folder, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()

    barcode = reader.decode("./aztec/upload/" + file.filename)

    return barcode
