
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.menu_repository import MenuRepository
from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import OrderService

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])


def get_order_service(db: Session = Depends(get_db)):
    menu_repository = MenuRepository(db)
    order_repository = OrderRepository(db)

    return OrderService(
        menu_repository=menu_repository,
        order_repository=order_repository,
    )


@router.get("/", response_model=list[OrderResponse])
def get_orders(
    service: OrderService = Depends(get_order_service),
):
    return service.get_all_orders()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    service: OrderService = Depends(get_order_service),
):
    order = service.get_order_by_id(order_id)

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pesanan tidak ditemukan",
        )

    return order


@router.post(
    "/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    order_data: OrderCreate,
    service: OrderService = Depends(get_order_service),
):
    try:
        return service.create_order(order_data.model_dump())
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error
