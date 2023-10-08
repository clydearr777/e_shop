"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard
from src.InstantiateCSVError import InstantiateSCVError
import pytest


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
# def test_name():
#     """ CaseTest for Homework-2  setter name"""
#     assert Item.name('ЭтоОченьДлинноеИмя') == 'ЭтоОченьДл'

def test__repr__():
    """ Test homework-3"""
    test = Item('Плеер', 100, 1)
    assert test.__repr__() == "Item('Плеер', 100, 1)"
def test__str__():
    """Test homework-3"""
    test = Item('Овощерезка', 50, 900)
    assert test.__str__() == 'Овощерезка'


def test__add__():
    """ Test homework-4"""
    phone1 = Phone('Dexp', 1000, 7, 2)
    item1 = Phone("Tix", 2000, 3, 1)
    assert Phone.__add__(phone1, item1) == 10

def test__repr__():
    """TestCase homework-4"""
    test = Phone("Xioami", 1000, 1, 2)
    assert test.__repr__() == "Phone('Xioami', 1000, 1, 2)"

def test__repr__():
    """TestCase homework-5"""
    test = Keyboard('Sven', 999, 9)
    assert test.__repr__() == "Keyboard('Sven', 999, 9)"


def test__add__():
    """TestCase homework-5"""
    keyboard1 = Keyboard('Sven', 9, 2)
    item1 = Phone('Iphone X', 90, 8, 3)
    assert Keyboard.__add__(keyboard1, item1) == 10

def test_change_lang():
    """TestCase homework-5"""
    key1 = Keyboard('Sven', 888, 8)
    assert key1.language == "EN"

def test_InstantiateSCVError():
    with pytest.raises(InstantiateSCVError):
        Item.instantiate_from_csv(1, path='../src/wrong_item.csv')

def test_instantiate_from_scv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(1, 'file.txt')




