
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.menu_repository import MenuRepository
from app.schemas.menu import MenuCreate, MenuResponse
from app.services.menu_service import MenuService

router = APIRouter(prefix="/api/v1/menus", tags=["Menus"])


def get_menu_service(db: Session = Depends(get_db)):
    repository = MenuRepository(db)
    return MenuService(repository)


@router.get("/", response_model=list[MenuResponse])
def get_menus(service: MenuService = Depends(get_menu_service)):
    return service.get_all_menus()


@router.get("/{menu_id}", response_model=MenuResponse)
def get_menu(
    menu_id: int,
    service: MenuService = Depends(get_menu_service),
):
    menu = service.get_menu_by_id(menu_id)

    if menu is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu tidak ditemukan",
        )

    return menu


@router.post(
    "/",
    response_model=MenuResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_menu(
    menu_data: MenuCreate,
    service: MenuService = Depends(get_menu_service),
):
    return service.create_menu(menu_data.model_dump())


@router.put("/{menu_id}", response_model=MenuResponse)
def update_menu(
    menu_id: int,
    menu_data: MenuCreate,
    service: MenuService = Depends(get_menu_service),
):
    menu = service.update_menu(menu_id, menu_data.model_dump())

    if menu is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu tidak ditemukan",
        )

    return menu


@router.delete("/{menu_id}")
def delete_menu(
    menu_id: int,
    service: MenuService = Depends(get_menu_service),
):
    deleted = service.delete_menu(menu_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu tidak ditemukan",
        )

    return {
        "message": "Menu berhasil dihapus",
        "id": menu_id,
    }
