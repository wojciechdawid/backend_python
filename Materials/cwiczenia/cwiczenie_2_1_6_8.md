
####  📝 Ćwiczenie - operator is

[Cwiczenie 2_1_6_8](cwiczenia/cwiczenie_2_1_6_8.md)


Operator `==` w Pythonie porównuje wartość obiektów, podczas gdy operator `is` porównuje ich tożsamość, tzn. czy obie zmienne wskazują na ten sam obiekt w pamięci. Ta subtelna różnica staje się szczególnie istotna przy porównywaniu wartości typu `bool`.


1. Stwórz dwie zmienne: jedną przypisując wartość `True` i drugą jako wynik wyrażenia logicznego, które również zwraca `True`:
   ```python
   a = True
   b = 1 == 1
   ```

2. Porównaj te dwie zmienne za pomocą operatora `==` oraz `is`:
   ```python
   print(a == b)  # Sprawdź wartość
   print(a is b)  # Sprawdź tożsamość
   ```

3. Oczekiwany wynik:
   - Pierwsze porównanie powinno zwrócić `True`, ponieważ obie zmienne mają wartość `True`.
   - Drugie porównanie również powinno zwrócić `True`, ponieważ w Pythonie istnieje tylko jedna instancja `True` i obie zmienne wskazują na ten sam obiekt.

4. Teraz stwórz dwie zmienne, używając wartości liczbowych tak, aby jedna z nich była traktowana jako prawda, a druga jako fałsz:
   ```python
   c = 1
   d = 0
   ```

5. Porównaj wartość logiczną zmiennej `c` z wartością `True` oraz wartość logiczną zmiennej `d` z wartością `False` za pomocą obu operatorów:
   ```python
   print(c == True)  # Sprawdź wartość
   print(c is True)  # Sprawdź tożsamość
   print(d == False) # Sprawdź wartość
   print(d is False) # Sprawdź tożsamość
   ```

6. Oczekiwany wynik:

- Pierwsze i trzecie porównanie powinny zwrócić `True`, ponieważ wartość liczby `1` jest traktowana jako prawda, a wartość liczby `0` jako fałsz w kontekście logicznym.
- Drugie i czwarte porównanie powinny zwrócić `False`, ponieważ mimo że liczby `1` i `0` są traktowane odpowiednio jako prawda i fałsz, nie są one tym samym obiektem co `True` i `False`.

To ćwiczenie ilustruje, jak ważne jest zrozumienie różnicy między porównywaniem wartości a tożsamości w Pythonie, zwłaszcza gdy pracujemy z wartościami logicznymi. Dzięki temu możemy unikać subtelnych błędów w naszym kodzie.
