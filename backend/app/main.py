from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# 環境変数の読み込み (.env ファイルから)
load_dotenv()

# DB接続設定
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True, future=True)

# FastAPI アプリケーションの作成
app = FastAPI()

# Pydantic モデル
class Item(BaseModel):
    name: str
    description: str | None = None

# ルートエンドポイント
@app.get("/")
def read_root():
    return {"message": "API is running"}

# POSTエンドポイントの例（Pydantic使用）
@app.post("/items/")
def create_item(item: Item):
    return {"received": item}

# DB接続確認用エンドポイント
@app.get("/db-check/")
def check_database():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"db_response": result.scalar()}
    except Exception as e:
        return {"error": str(e)}