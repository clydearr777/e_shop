import csv
from src.InstantiateCSVError import InstantiateSCVError


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

    @property
    def name(self):
        """homework-2 Геттер для приватного параметра __name"""
        return self.__name

    @name.setter
    def name(self, name):
        """ Homework-2 метод проверяет количество символов в параметре __name и обрезает в случае если их >10"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Homework-2
        Инициализирует экземпляры класса данными из файла
        """
        Item.all = []
        path = f'../{path}'
        with open(path, newline='') as f:
            file = csv.DictReader(f)
            for info in file:
                Item(info['name'], info['price'], info['quantity'])

    @staticmethod
    def string_to_number(number):
        """ HOMEWORK-2  Возвращает число (int) вместо строки"""
        return int(float(number))

    def __repr__(self):
        """ Homework-3 Метод возвращение в виде 'Название класса(имя, цена, кол-во)"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Homewokr-3 магический метод __str__"""
        return self.__name

    def __add__(self, other):
        """ homework-4 метод реализует суммирование экземплров класса по количеству в магазине"""
        return self.quantity + other.quantity

    def calculate_total_price(self):
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
    def instantiate_from_csv(cls, number=1, path='../src/items.csv'):
        """ Метод класса дл исключений  """
        try:
            with open(path) as file:
                d_csv = csv.DictReader(file)
                len_of_dict = len(d_csv.fieldnames)
                dict_used = []
                if len_of_dict != 3:
                    raise InstantiateSCVError('InstantiateCSVError: Файл item.csv поврежден')
                for element in d_csv:
                    dict_used.append(element)

                    if number < 1 or number > 5:
                        number = 1
                    name = dict_used[number - 1]["name"]
                    price = int(dict_used[number - 1]["price"])
                    quantity = int(dict_used[number - 1]["quantity"])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except (ValueError, KeyError):
            raise InstantiateSCVError('Файл item.csv поврежден')
        return cls(name, price, quantity)





