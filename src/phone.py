from src.item import Item


class Phone(Item):
    """
    класс-наследник от класса ITEM
    параметр number_of_sim - количество сим-карт
    """

    # number_of_sim = 1
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        number_of_sim: int = 1

    # @number_of_sim.setter
    # def number_of_sim(self, sim):
    #     pass

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
