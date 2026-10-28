
from app.repositories.menu_repository import MenuRepository


class MenuService:
    def __init__(self, repository: MenuRepository):
        self.repository = repository

    def get_all_menus(self):
        return self.repository.get_all()

    def get_menu_by_id(self, menu_id: int):
        return self.repository.get_by_id(menu_id)

    def create_menu(self, menu_data: dict):
        return self.repository.create(menu_data)

    def update_menu(self, menu_id: int, menu_data: dict):
        return self.repository.update(menu_id, menu_data)

    def delete_menu(self, menu_id: int):
        return self.repository.delete(menu_id)
