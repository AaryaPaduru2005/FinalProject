# api/main.py

from fastapi import FastAPI
from dotenv import load_dotenv
from api.dependencies.database import Base, engine
from api.routers import ingredients, menu, promotions, reviews, orders

# Make sure .env is loaded so DATABASE_URL is set
load_dotenv()

app = FastAPI(title="OROS API")

@app.on_event("startup")
def startup():
    # This will create any missing tables—but only *after* your create_db.py
    # has dropped & re-created them with the right columns.
    Base.metadata.create_all(bind=engine)

# register all routers
app.include_router(ingredients.router)
app.include_router(menu.router)
app.include_router(promotions.router)
app.include_router(reviews.router)
app.include_router(orders.router)
