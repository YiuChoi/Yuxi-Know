import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router
from src.utils.logging_config import setup_logger

load_dotenv()

import os

os.environ["ZHIPUAI_API_KEY"] = "270ea71e9560c0ff406acbcdd48bfd97.e3XOMdWKuZb7Q1Sk"

app = FastAPI()
app.include_router(router)

# CORS 设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logger = setup_logger("server:main")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

