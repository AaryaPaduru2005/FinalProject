# create_db.py

import os
from sqlalchemy import create_engine, text
from api.dependencies.database import Base

# 1) Import *all* your models so SQLAlchemy knows about them
import api.models.ingredient
import api.models.menu_item
import api.models.menu_item_ingredient
import api.models.order
import api.models.order_item
import api.models.promotion
import api.models.review

# 2) Ensure the database exists
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:Foxtropostal4567!@localhost/"
)
if not DATABASE_URL.endswith("/"):
    DATABASE_URL = DATABASE_URL.rsplit("/", 1)[0] + "/"

engine_server = create_engine(DATABASE_URL, echo=True)
with engine_server.connect() as conn:
    conn.execute(text("""
        CREATE DATABASE IF NOT EXISTS oros_db
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci
    """))
    print("✅ Ensured database oros_db exists.")

# 3) Drop & recreate all tables inside oros_db
DB_URL = DATABASE_URL + "oros_db"
engine_db = create_engine(DB_URL, echo=True)

Base.metadata.drop_all(bind=engine_db)
print("🗑 Dropped all tables in oros_db")

Base.metadata.create_all(bind=engine_db)
print("✅ Created all tables in oros_db")
