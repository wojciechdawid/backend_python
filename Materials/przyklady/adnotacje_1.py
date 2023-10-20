from decimal import Decimal


Numeric = int | float | Decimal | str


def CzDodatnia(value: Numeric) -> bool:
    if isinstance(value, (int, float, Decimal)):
        return value > 0
    return NotImplemented


CzDodatnia(1)
CzDodatnia(1.2)
CzDodatnia(Decimal("1"))
CzDodatnia("a")
