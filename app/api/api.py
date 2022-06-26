from __future__ import annotations

from http.client import HTTPResponse
from typing import Union

from starlette.responses import JSONResponse

from fastapi import APIRouter
from app.services import post_imports, delete_id, get_product_by_id, get_data_products
from app.api.schemas import Error, ShopUnit, ShopUnitImportRequest, ShopUnitType

router = APIRouter()


@router.post('/imports', response_model=None, status_code=200, responses={'400': {'model': Error}})
def create_product_route(product_create: ShopUnitImportRequest):
    post_imports(product_create.items, product_create.updateDate)
    return JSONResponse(content={"description": 'Вставка или обновление прошли успешно.'}, status_code=200)


@router.delete('/delete/{id}', response_model=None, responses={'400': {'model': Error}, '404': {'model': Error}})
def delete_delete_id(id: str) -> Union[None, Error]:
    delete_id(id)
    return JSONResponse(content={"description": "Удаление прошло успешно."}, status_code=200)


@router.get('/nodes/{id}', response_model=ShopUnit, responses={'400': {'model': Error}, '404': {'model': Error}})
def get_nodes_id(id: str):
    product = get_data_products(id)
    return product[0]
