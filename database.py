from sqlalchemy import create_create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. تحديد رابط الاتصال بقاعدة البيانات (المستخدم، كلمة المرور، الخادم، اسم قاعدة البيانات)
# نستخدم محرك pymysql الذي قمنا بتثبيته سابقاً
DATABASE_URL = "mysql+pymysql://asset_user:SecureDevOpsPass2026!@localhost/asset_tracker_db"

# 2. إنشاء محرك الاتصال (Engine) الذي يتعامل مباشرة مع السيرفر
engine = create_engine(DATABASE_URL)

# 3. إنشاء جلسة عمل (Session) مجهزة للتعامل مع العمليات (إدخال، حذف، تعديل)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. الفئة الأساسية (Base) التي سترث منها جميع جداول قاعدة البيانات لاحقاً
Base = declarative_base()

# دالة مساعدة لفتح وإغلاق الاتصال تلقائياً مع كل طلب (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
