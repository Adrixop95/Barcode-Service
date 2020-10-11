from pydantic import BaseModel, Field


class Barcode(BaseModel):
    barcode_type: str = Field(..., title="Barcode type")
    barcode_message: str = Field(..., title="Barcode message")
