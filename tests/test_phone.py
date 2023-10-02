from src.phone import Phone


def test__repr__():
    """TestCase homework-4"""
    test = Phone("Xioami", 1000, 1, 2)
    assert test.__repr__() == "Phone('Xioami', 1000, 1, 2)"



