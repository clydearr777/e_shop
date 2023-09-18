"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price():
    test1 = Item('Электробритва', 1000, 10)
    res = test1.price * test1.quantity
    assert test1.calculate_total_price() == res

def test_apply_discount():
    test2 = Item('Плойка', 1000, 5)
    test2.pay_rate = 0.85
    discount_price = test2.price * test2.pay_rate
    assert test2.apply_discount() == discount_price

def test_string_to_number():
    """ caseTest for Homework-2, получаем из строки - число"""
    assert Item.string_to_number("9.25") == 9
def test_name():
    """ CaseTest for Homework-2  setter name"""
    assert Item.name('ЭтоОченьДлинноеИмя') == 'ЭтоОченьДл'

def test__repr__():
    test = Item('Плеер', 100, 1)
    assert test.__repr__() == "Item('Плеер', 100, 1)"
def test__str__():
    test = Item('Овощерезка', 50, 900)
    assert test.__str__() == 'Овощерезка'
