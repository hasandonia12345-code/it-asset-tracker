from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Asset(Base):
    # اسم الجدول الفعلي في قاعدة البيانات
    __tablename__ = "assets"

    # الحقول والمحددات (Columns)
    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(100), unique=True, nullable=False, index=True)
    ip_address = Column(String(50), nullable=False)
    os_version = Column(String(50), nullable=False)  # مثلاً: RHEL 7.4 أو Ubuntu 22.04
    status = Column(String(20), default="Active")     # حالة السيرفر: Active, Offline, Maintenance
    created_at = Column(DateTime, default=datetime.utcnow)
