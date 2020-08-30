from fastapi import APIRouter
from pydantic import BaseModel
from aztec_code_generator import AztecCode
from starlette.responses import FileResponse

router = APIRouter()


class Aztec(BaseModel):
    aztec_code_scale: int
    aztec_code_message: str


@router.post("/generate")
async def aztec_code_image(aztec_gen: Aztec):
    message_filename = "./aztec/" + aztec_gen.aztec_code_message.replace('/', '') + ".png"

    aztec_code = AztecCode(message_filename)
    aztec_code.save(message_filename, aztec_gen.aztec_code_scale)
    return FileResponse(message_filename)

