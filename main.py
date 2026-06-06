from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db

# إنشاء الجداول
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="IT Asset Tracker API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to IT Asset Tracker Engine V1"}


# مسار إضافة سيرفر جديد (POST API)
@app.post("/assets/", response_model=schemas.AssetResponse)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    
    # 1. التحقق من أن الـ hostname غير مسجل مسبقاً في النظام
    db_asset = db.query(models.Asset).filter(models.Asset.hostname == asset.hostname).first()
    if db_asset:
        raise HTTPException(status_code=400, detail="Hostname already registered in your infrastructure")
    
    # 2. تحويل البيانات القادمة من الـ API إلى كائن يفهمه الـ ORM
    new_asset = models.Asset(
        hostname=asset.hostname,
        ip_address=asset.ip_address,
        os_version=asset.os_version,
        status=asset.status
    )
    
    # 3. حفظ البيانات في MySQL داخل الـ Session
    db.add(new_asset)
    db.commit()      # تثبيت التغييرات
    db.refresh(new_asset) # جلب البيانات المحدثة (مثل الـ ID والوقت) لإرجاعها للمستخدم
    
    return new_asset
