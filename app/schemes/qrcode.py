from pydantic import BaseModel, Field


class QRCode(BaseModel):
    qrcode_scale: int = Field(..., title="QRCode scale")
    qrcode_message: str = Field(..., title="QRCode message")
    qrcode_error_correct: str = Field(None, title="QRCode error correct")
