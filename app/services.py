from datetime import datetime
from http.client import HTTPException
from uuid import UUID
from fastapi import HTTPException
from dependency_injector.wiring import inject, Provide

from app.api.schemas import ShopUnit
from containers import Container
from app.database.exceptions import NotFoundException

from app.database.unit_of_work import UnitOfWork
from app.database.schema import Product


@inject
def post_imports(items: list, updateDate: str, unit_of_work: UnitOfWork = Provide[Container.products_uow]):
    with unit_of_work:
        for i in range(len(items)):
            try:
                db_product = unit_of_work.repository.get(id=items[i].id)
                db_product.name = items[i].name
                db_product.parentId = items[i].parentId
                db_product.type = items[i].type
                db_product.price = items[i].price
                db_product.updateDate = updateDate
            except NotFoundException:
                db_product = Product(id=items[i].id, name=items[i].name, parentId=items[i].parentId,
                                     type=items[i].type, price=items[i].price, updateDate=updateDate)
            unit_of_work.repository.save(db_product)

        unit_of_work.commit()


@inject
def delete_id(id: UUID, unit_of_work: UnitOfWork = Provide[Container.products_uow]):
    with unit_of_work:
        try:
            product = unit_of_work.repository.get(id=id)
            unit_of_work.repository.delete(id=id)
            if product.type and product.type.name == 'CATEGORY':
                unit_of_work.repository.delete_by_parent_id(id=id)
            unit_of_work.commit()
        except:
            raise HTTPException(status_code=404, detail="Категория/товар не найден.")


@inject
def get_product_by_id(id: int, unit_of_work: UnitOfWork = Provide[Container.products_uow]):
    with unit_of_work:
        try:
            product = unit_of_work.repository.get(id=id)
            product.children = []
            product.date = datetime.now()
            if product.type and product.type.name == 'CATEGORY':
                price = 0
                items = unit_of_work.repository.get_by_parent_id(id=id)
                for i in range(len(items)):
                    product.children.append(items[i])
                product.price = price
            return product


        except NotFoundException as exc:
            raise HTTPException(status_code=404, detail="Категория/товар не найден.")


def get_data_products(id):
    """Напишем функцию, которая будет проходиться по всем данным"""
    product = get_product_by_id(id=id)
    children_data = None
    sum = 0
    count = 0

    if product.type and product.type.name == 'CATEGORY':
        children_data = []
        for i in range(len(product.children)):
            full_data = get_data_products(product.children[i].id)
            data = full_data[0]
            children_data.append(data)

            if type(product.children[i].price) is int:
                sum += product.children[i].price
                count += 1
            else:
                sum += full_data[1]
                count += full_data[2]

        if sum != 0 and count != 0:
            product.price = round(sum / count)

    product = ShopUnit(id=product.id, name=product.name, date=product.date, parentId=product.parentId,
                       type=(product.type.name), children=children_data, price=product.price)

    return product, sum, count
