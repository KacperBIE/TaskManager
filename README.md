# Task Manager w Pythonie

Aplikacja konsolowa do zarządzania listami zadań (TO-DO) z obsługą wielu list, zapisem do pliku oraz automatycznym ukrywaniem ukończonych zadań po określonym czasie.

## Funkcjonalności
- Dodawanie zadań do list
- Wyświetlanie list zadań
- Usuwanie zadań
- Oznaczanie zadań jako ukończone
- Obsługa wielu list
- Automatyczne ukrywanie ukończonych zadań po upływie określonego czasu (domyślnie 1 dzień)
- Możliwość ponownego wyświetlania ukrytych zadań

## Wymagania
- Python 3.6+

## Instalacja
Pobierz skrypt `tm.py` i umieść go w dowolnym katalogu.

## Użycie
Aby uruchomić aplikację, użyj poniższych komend w terminalu:

### Dodawanie zadania
```sh
py tm.py dodaj <nazwa_listy> "Treść zadania"
```
Przykład:
```sh
py tm.py dodaj Praca "Przygotować raport"
```

### Wyświetlanie listy zadań
```sh
py tm.py lista <nazwa_listy>
```
Przykład:
```sh
py tm.py lista Praca
```
Aby pokazać ukryte zadania, dodaj flagę `--pokaz-ukryte`:
```sh
py tm.py lista Praca --pokaz-ukryte
```

### Usuwanie zadania
```sh
py tm.py usun <nazwa_listy> <numer_zadania>
```
Przykład:
```sh
py tm.py usun Praca 1
```

### Oznaczanie zadania jako ukończone
```sh
py tm.py ukoncz <nazwa_listy> <numer_zadania>
```
Przykład:
```sh
py tm.py ukoncz Praca 1
```

## Przechowywanie danych
Wszystkie listy zadań są zapisywane w jednym pliku `zadania.json`, co umożliwia ich trwałe przechowywanie między uruchomieniami programu.

## Uwagi
- Domyślnie ukończone zadania są ukrywane po 24 godzinach. Można je ponownie wyświetlić za pomocą `--pokaz-ukryte`.
- Jeśli plik `zadania.json` nie istnieje, zostanie utworzony automatycznie.


