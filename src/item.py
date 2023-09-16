import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self.__name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 0:
            name = name[:10]
        self.__name = name

    name = property(get_name, set_name)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Инициализирует экземпляры класса данными из файла
        """
        with open(path, 'r') as f:
            file = csv.DictReader(f)
            for info in file:
                Item(info['name'],info['price'],info['quantity'])

    def string_to_number(number):
        return int(float(number))

