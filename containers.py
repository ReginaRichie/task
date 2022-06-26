from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory

from app.database.sessions import Session
from app.database.unit_of_work import AlchemyUnitOfWork
from app.database.product_repository import ProductRepository


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=['app', ]
    )

    session_creator = Factory(Session)

    products_repository = Factory(
        ProductRepository,
        session=session_creator,
    )

    products_uow = Factory(
        AlchemyUnitOfWork,
        repository=products_repository,
    )
