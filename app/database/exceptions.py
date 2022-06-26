# from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound
from starlette.responses import JSONResponse


class NotFoundException(NoResultFound):
    pass