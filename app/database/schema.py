from datetime import datetime

from sqlalchemy.orm import relationship

from app.database.database_setup import Base
from sqlalchemy import (
    Column, ForeignKey, ForeignKeyConstraint, Integer, String
)

from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
import enum
from sqlalchemy import Enum


class ShopUnitType(enum.Enum):
    OFFER = 'OFFER'
    CATEGORY = 'CATEGORY'

# объединение таблиц
# class Relations(Base):
#     __tablename__ = "relations"
#     import_id = Column(Integer, ForeignKey("import.import_id"), nullable=False)
#     parent_id = Column(UUID(as_uuid=True), ForeignKey("products.parent_id"), nullable=False)
#     id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
#
#

# история операций
# class ProductImport(Base):
#     __tablename__ = "imports"
#     id = Column(Integer, autoincrement=True, primary_key=True, index=True)
#     updateDate = Column(TIMESTAMP(timezone=True), index=True)
#     items = relationship("Product", back_populates="owner")

# основная таблица
class Product(Base):
    __tablename__ = "products"
    #import_id = Column(Integer, ForeignKey("imports.id"), primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    parentId = Column(UUID(as_uuid=True), nullable=True, index=True)
    name = Column(String(1200), nullable=False)
    price = Column(Integer, nullable=True, default=None)
    type = Column(Enum(ShopUnitType), nullable=False)
    date = Column(TIMESTAMP(timezone=True), index=True, default=datetime.now())
    updateDate = Column(TIMESTAMP(timezone=True), index=True)
    #owner = relationship("ProductImport", backref="items")
    # __table_args__ = (ForeignKeyConstraint([import_id, parentId], [import_id, id], ondelete="CASCADE"),)

