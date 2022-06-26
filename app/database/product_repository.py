from app.database.repository import Repository
from app.database.schema import Product
from sqlalchemy.orm.exc import NoResultFound
from app.database.exceptions import NotFoundException


class ProductRepository(Repository):
    def get(self, id: int):
        try:
            return self.session.query(Product).filter_by(id=id).one()
        except NoResultFound as exc:
            raise NotFoundException(exc)

    def get_by_parent_id(self, id: int):
        try:
            return self.session.query(Product).filter_by(parentId=id).all()

        except NoResultFound as exc:
            raise NotFoundException(exc)

    def list(self):
        return self.session.query(Product).all()

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        self.session.add(obj)

    def delete(self, id: int):
        try:
            entity: Product = self.session.query(Product).filter_by(id=id).one()
            self.session.delete(entity)
        except NoResultFound as exc:
            raise NotFoundException(exc)

    def delete_by_parent_id(self, id: int):
        try:
            entity: Product = self.session.query(Product).filter_by(parentId=id).all()
            for i in range(len(entity)):
                self.session.delete(entity[i])
        except NoResultFound as exc:
            raise NotFoundException(exc)
