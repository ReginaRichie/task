from __future__ import annotations

from fastapi import FastAPI, Query

import typing

import uvicorn
from starlette.responses import JSONResponse

from containers import Container
from app.api.api import router as products_router


class CustomResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return super(CustomResponse, self).render({
            "data": content,
            "version": "1.0.0",
        })


app = FastAPI(
    description='Вступительное задание в Летнюю Школу Бэкенд Разработки Яндекса 2022',
    title='Mega Market Open API',
    version='1.0',
    default_response_class=CustomResponse,
)

# app.include_router(products_router, prefix='/products')
app.include_router(products_router)

container = Container()

if __name__ == '__main__':
    uvicorn.run(app)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=80)

# на `0.0.0.0:80`

