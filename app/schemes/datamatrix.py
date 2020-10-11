from pydantic import BaseModel, Field


class DataMatrix(BaseModel):
    data_matrix_message: str = Field(..., title="Data matrix message")
