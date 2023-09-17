import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_router import api_router

app = FastAPI(root_path="/api/v1", version="0.1.6")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.on_event("startup")
async def create_folder_structure():
    folders = ['./barcode', './qrcode', './aztec', './aztec/upload', './datamatrix']
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
