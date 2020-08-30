from fastapi import APIRouter, File
from pydantic import BaseModel
from starlette.responses import FileResponse
from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image
from io import BytesIO

router = APIRouter()


class DataMatrix(BaseModel):
    data_matrix_message: str


@router.post("/generate")
async def data_matrix_image_generate(data_gen: DataMatrix):
    message_filename = "./datamatrix/" + data_gen.data_matrix_message.replace('/', '') + ".png"

    encoded = encode(data_gen.data_matrix_message.encode('utf-8'))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save(message_filename)
    return FileResponse(message_filename)


@router.post("/decrypt")
async def data_matrix_image_decrypt(file: bytes = File(...)):
    stream = BytesIO(file)
    img = Image.open(stream)

    return decode(img)
