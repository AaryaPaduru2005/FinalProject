from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.dependencies.database import get_db
from api.schemas.menu_item import MenuItem, MenuItemCreate, MenuItemUpdate
from api.controllers.menu import get_menu_items, get_menu_item, create_menu_item, update_menu_item, delete_menu_item

router = APIRouter(tags=["menu"])


@router.get("/", response_model=List[MenuItem])
def read_menu(category: str = None, db: Session = Depends(get_db)):
    items = get_menu_items(db)
    if category:
        items = [i for i in items if i.category == category]
    return items

@router.get("/{item_id}", response_model=MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    return get_menu_item(db, item_id)

@router.post("/", response_model=MenuItem, status_code=201)
def add_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    return create_menu_item(db, item)

@router.put("/{item_id}", response_model=MenuItem)
def edit_menu_item(item_id: int, data: MenuItemUpdate, db: Session = Depends(get_db)):
    return update_menu_item(db, item_id, data)

@router.delete("/{item_id}", status_code=204)
def remove_menu_item(item_id: int, db: Session = Depends(get_db)):
    delete_menu_item(db, item_id)
