
#### 📝 Ćwiczenie: operator `:=`

[Cwiczenie 1_4_9_1](cwiczenia/cwiczenie_1_4_9_1.md)


```python

if x := 1 < 2:
    print("udało się")
print(x)

```

Masz daną listę liczb i chcesz znaleźć pierwszą liczbę większą od 10, a jednocześnie chcesz wiedzieć, na którym miejscu w liście ta liczba się znajduje.

1. Utwórz listę liczb:
   ```python
   liczby = [7, 3, 12, 5, 14, 8, 9]
   ```

2. Używając pętli `while` i operatora walrusa, znajdź pierwszą liczbę większą od 10 oraz jej indeks:

   ```python
   indeks = 0

   # tu twoja implementacja

   if indeks < len(liczby):
       print(f"Pierwsza liczba większa od 10 to {liczba}, znajdująca się na pozycji {indeks}.")
   else:
       print("Nie znaleziono liczby większej od 10 w liście.")
   ```

Sprawdź rozwiązanie dla różnych list.
