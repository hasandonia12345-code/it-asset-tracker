from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# الهيكل المشترك للأصول
class AssetBase(BaseModel):
    hostname: str
    ip_address: str
    os_version: str
    status: Optional[str] = "Active"

# الهيكل المطلوب عند إنشاء أصل جديد (المدخلات)
class AssetCreate(AssetBase):
    pass

# الهيكل الذي سيرد به الـ API على المستخدم (المخرجات)
# نزيد عليه الـ id ووقت الإنشاء لأن قاعدة البيانات هي من تولدهم
class AssetResponse(AssetBase):
    id: int
    created_at: datetime

    class Config:
        # لتفعيل التوافقية بين مخرجات SQLAlchemy و Pydantic
        from_attributes = True
