from src.item import Item


class Phone(Item):
    """
    класс-наследник от класса ITEM
    параметр number_of_sim - количество сим-карт
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        try:
            if number_of_sim <= 0 or number_of_sim is not int:
                raise ValueError()
            else:
                self.number_of_sim = number_of_sim
        except ValueError:
            print("Количество физических SIM-карт должно быть целым числом больше нуля.")
        super().__init__(name, price, quantity)



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"




