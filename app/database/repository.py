from abc import ABC, abstractmethod


class Repository(ABC):
    def __init__(self, session):
        self.session = session

    # отдельный продукт взять
    @abstractmethod
    def get(self, id: int):
        raise NotImplementedError()

    # взять много продуктов
    @abstractmethod
    def list(self):
        raise NotImplementedError()

    # сохранить продукт
    @abstractmethod
    def save(self, obj):
        raise NotImplementedError()

    # обновить данные по продукту
    @abstractmethod
    def update(self, obj):
        raise NotImplementedError()