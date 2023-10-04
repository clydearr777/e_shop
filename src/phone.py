from src.item import Item


class Phone(Item):
    """
    класс-наследник от класса ITEM
    параметр number_of_sim - количество сим-карт
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        # try:
        #     if self.number_of_sim <= 0:
        #         raise ValueError()
        # except ValueError:
        #     print('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        """homework-4 Геттер для параметра __number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Сеттер для атрибута количества симкарт
        параметр не должен быть меньше либо равен нулюи должен быть целым числом"""
        if value <= 0 and isinstance(value, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = value

    def __repr__(self):
        """ Homework-4 Метод возвращение в виде 'Название класса(имя, цена, кол-во, сим-карты)"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


