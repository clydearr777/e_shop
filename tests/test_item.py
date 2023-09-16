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
