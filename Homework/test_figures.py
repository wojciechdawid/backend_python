import pytest
import figures as f

def test_add_classes():
    c1 = f.Circle(5)
    s1 = f.Square(10)
    c2 = c1 + s1
    assert c2.radius == 7.54
