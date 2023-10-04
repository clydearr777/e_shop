from src.item import Item


class Mixin:
    """ Класс-миксин для добавления метода переключения языка
        дополнительного параметра - language, по умолчанию -EN + сеттер """
    __language = 'EN'

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def language(self):
        """
        Геттер для параметра language, по умолчанию - EN, далее переключение языка
        возможно только через метод change_lang
        """

        return self.__language

    @language.setter
    def language(self, value):
        """Сеттер для атрибута языка клавиатуры
        параметр не может принимать значения кроме RU и EN"""
        if value != 'EN' or value != 'RU':
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        else:
            self.__language = value

    def change_lang(self) -> None:
        """
        метод, для переключения языка (иначе никак)
        """
        if self.__language == 'EN':
            self.__language = 'RU'
            print('переключили На русский')
        else:
            self.__language = 'EN'
            print('переключили На англ')


class Keyboard(Mixin, Item):
    """
     класс-наследник от класса ITEM
     param: имя, цена, количество
     """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)


