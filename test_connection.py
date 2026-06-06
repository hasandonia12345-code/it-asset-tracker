import pymysql
# ملاحظة: في المشاريع الحقيقية نضع هذه البيانات في ملف .env مخفي
try:
    connection = pymysql.connect(
        host='localhost', user='asset_user',
        password='SecureDevOpsPass2026!', database='asset_tracker_db'
    )
    print("✅ Connection Successful!")
    connection.close()
except Exception as e:
    print(f"❌ Error: {e}")
