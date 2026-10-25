
from fastapi import FastAPI

from app.routers.orders import router as order_router
from app.routers.menus import router as menu_router

from app.database import Base, engine
from app.models.menu import Menu
from app.models.order import Order, OrderItem

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistem Pemesanan Makanan Kantin",
    description="REST API untuk mengelola menu dan pesanan makanan kantin.",
    version="1.0.0",
)


app.include_router(menu_router)
app.include_router(order_router)


@app.get("/")
def home():
    return {
        "message": "Selamat datang di API Pemesanan Makanan Kantin",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
