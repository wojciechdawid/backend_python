
### 📝 Ćwiczenie: Analiza Danych z pliku CSV

[Cwiczenie_4_4_5](cwiczenia/cwiczenie_4_4_5.md)



**Opis zadania:**

Twoim zadaniem jest przetworzenie danych z pliku CSV zawierającego informacje o produktach w sklepie spożywczym. Plik CSV ma następującą strukturę:

```
Produkt,Kategoria,Cena,Ilość
Chleb,Pieczywo,2.50,10
Mleko,Nabiał,1.20,20
Jajka,Nabiał,1.80,30
Pomarańcze,Owoce,2.00,15
...
```

Twoje zadanie składa się z trzech części:

#### Przygotowanie - zapis danych do pliku

#### Część 1

Napisz skrypt w Pythonie, który wczytuje dane z pliku CSV i używa wyrażenia zrozumiałego do stworzenia słownika, gdzie kluczem jest nazwa kategorii, a wartością jest lista produktów należących do tej kategorii. Na przykład:

```python
{
    'Pieczywo': ['Chleb'],
    'Nabiał': ['Mleko', 'Jajka'],
    'Owoce': ['Pomarańcze'],
    ...
}
```

**Część 2:**

Napisz generator, który generuje informacje o produktach, których cena przekracza określoną wartość. Generator powinien generować te informacje na żądanie, aby uniknąć wczytywania wszystkich danych do pamięci naraz.

Po zakończeniu zadania, skrypt powinien wypisać informacje o produktach, których cena przekracza 2.00 złotych.

**Wskazówki:**

1. Możesz użyć modułu `csv` w Pythonie do wczytania danych z pliku CSV.

2. Wyrażenie zrozumiałe może pomóc w grupowaniu produktów według kategorii.

3. Generatory pozwalają na leniwe przetwarzanie danych, co jest przydatne przy dużych zbiorach danych.

4. Przemyśl, jak przechowywać dane w słowniku w taki sposób, aby były łatwo dostępne w części 2 zadania.

To zadanie pozwoli Ci praktycznie wykorzystać wyrażenia zrozumiałe do grupowania danych i generatory do przetwarzania dużych zbiorów danych w sposób efektywny.
