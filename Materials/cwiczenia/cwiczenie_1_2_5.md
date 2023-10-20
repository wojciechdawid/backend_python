### 📝 Ćwiczenie z użycia funkcji `help` i `dir` w Pythonie

[Cwiczenie 1_2_5](cwiczenia/cwiczenie_1_2_5.md)


**Cel:** Zrozumienie, jak korzystać z funkcji `help` i `dir` do eksploracji modułów, klas i funkcji w Pythonie.

**Kroki:**

1. **Eksploracja modułu standardowego**
    - Zaimportuj moduł `os`.
    - Użyj `dir(os)` do wyświetlenia listy dostępnych funkcji i atrybutów w module `os`.
    - Wybierz 3 funkcje z listy (na przykład: `os.getcwd`, `os.listdir`, `os.mkdir`).
    - Użyj `help(os.FUNKCJA)` dla każdej z trzech wybranych funkcji, aby zrozumieć, jak działają i jakie przyjmują argumenty.

2. **Eksploracja wbudowanej klasy**
    - Utwórz listę (np. `moja_lista = [1, 2, 3, 4]`).
    - Użyj `dir(moja_lista)` do wyświetlenia listy dostępnych metod dla obiektu typu lista.
    - Wybierz 3 metody z listy (na przykład: `append`, `pop`, `index`).
    - Użyj `help(moja_lista.METODA)` dla każdej z trzech wybranych metod, aby zrozumieć, jak działają.

3. **Stworzenie własnej klasy i eksploracja jej metod**
    - Utwórz prostą klasę:

    ```python
    class Samochod:
        def __init__(self, marka, model):
            self.marka = marka
            self.model = model
        
        def pokaz_info(self):
            return f"Samochód {self.marka} model {self.model}"
    ```

    - Użyj `dir(Samochod)` do wyświetlenia listy metod dla klasy `Samochod`.
    - Spróbuj użyć `help(Samochod.pokaz_info)`, aby zrozumieć, jak działa metoda `pokaz_info`.

**Zadanie dodatkowe:** Wypróbuj funkcję `dir` bez żadnych argumentów w interaktywnym interpreterze Pythona i zastanów się, co ona zwraca. Jakie zmienne i funkcje są dostępne w bieżącym zakresie?

**Podsumowanie:** Po zakończeniu tego ćwiczenia powinieneś być w stanie skutecznie korzystać z funkcji `help` i `dir` do eksploracji i zrozumienia różnych aspektów modułów, klas i funkcji w Pythonie.
