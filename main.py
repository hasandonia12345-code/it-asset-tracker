from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, get_db

# أمر سحري: يخبر SQLAlchemy بأن ينظر في ملف models وينشئ الجداول فوراً في MySQL
models.Base.metadata.create_all(bind=engine)

# بناء التطبيق
app = FastAPI(title="IT Asset Tracker API", version="1.0.0")

# مسار تجريبي سريع (Root Route) للتأكد من عمل الـ API
@app.get("/")
def read_root():
    return {"message": "Welcome to IT Asset Tracker Engine V1"}
