from pydantic import BaseModel, PositiveInt, Field


class Aztec(BaseModel):
    aztec_code_scale: PositiveInt = Field(..., title="Aztec qrcode scale")
    aztec_code_message: str = Field(..., title="Aztec qrcode message")
