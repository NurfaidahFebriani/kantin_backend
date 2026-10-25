
from sqlalchemy.orm import Session

from app.models.menu import Menu


class MenuRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Menu).all()

    def get_by_id(self, menu_id: int):
        return self.db.query(Menu).filter(
            Menu.id == menu_id
        ).first()

    def create(self, menu_data: dict):
        menu = Menu(**menu_data)

        self.db.add(menu)
        self.db.commit()
        self.db.refresh(menu)

        return menu

    def update(self, menu_id: int, menu_data: dict):
        menu = self.get_by_id(menu_id)

        if menu is None:
            return None

        for key, value in menu_data.items():
            setattr(menu, key, value)

        self.db.commit()
        self.db.refresh(menu)

        return menu

    def delete(self, menu_id: int):
        menu = self.get_by_id(menu_id)

        if menu is None:
            return False

        self.db.delete(menu)
        self.db.commit()

        return True
