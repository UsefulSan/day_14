from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, items: dict, capacity: int) -> None:
        self._items = items
        self._capacity = capacity

    @property
    def items(self) -> dict:
        """
        Возвращает словарь с товарами на складе.
        """
        return self._items

    @property
    def capacity(self) -> int:
        """
        Возвращает информацию о вместительности склада.
        """
        return self._capacity

    def add(self, name: str, quantity: int) -> None:
        """
        Добавляет товар
        """
        if name not in self.items:
            self.items[name] = quantity
        else:
            self.items[name] += quantity

    def remove(self, name: str, quantity: int) -> bool:
        """
        Проверяет на наличие количества товара и уменьшение/удаление
        """
        if quantity <= self.items[name]:
            self.items[name] -= quantity
            if self.items[name] == 0:
                del self.items[name]
            return True

    def get_free_space(self) -> int:
        """
        Возвращает количества свободного места
        """
        return self.capacity - sum(self.items.values())

    def get_unique_items_count(self) -> int:
        """
        Возвращает количество уникальных товаров.
        """
        return len(set(self.items))


class Store(Storage):  # склад

    def __init__(self, items: dict, capacity: int = 100) -> None:
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int) -> bool:
        if self.get_free_space() > quantity:
            super().add(name, quantity)
            return True


class Shop(Store):  # магазин

    def __init__(self, items: dict, capacity: int = 20) -> None:
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int) -> bool:
        if self.get_unique_items_count() < 5:
            super().add(name, quantity)
            return True


class Request:  # перемещение

    def __init__(self, from_: str, to: str, amount: int, product: str) -> None:
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self) -> str:
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"
