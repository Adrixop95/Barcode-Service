import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import aztecode_gen, barcode_gen, datamatrix_gen, qrcode_gen

app = FastAPI(version="0.1.3")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    aztecode_gen.router,
    prefix="/aztec"
)

app.include_router(
    barcode_gen.router,
    prefix="/barcode"
)

app.include_router(
    datamatrix_gen.router,
    prefix="/datamatrix"
)

app.include_router(
    qrcode_gen.router,
    prefix="/qrcode"
)


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
