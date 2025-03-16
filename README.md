# Lista TO-DO w Pythonie

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
Pobierz skrypt `todo.py` i umieść go w dowolnym katalogu.

## Użycie
Aby uruchomić aplikację, użyj poniższych komend w terminalu:

### Dodawanie zadania
```sh
python todo.py add <nazwa_listy> "Treść zadania"
```
Przykład:
```sh
python todo.py add Praca "Przygotować raport"
```

### Wyświetlanie listy zadań
```sh
python todo.py list <nazwa_listy>
```
Przykład:
```sh
python todo.py list Praca
```
Aby pokazać ukryte zadania, dodaj flagę `--show-hidden`:
```sh
python todo.py list Praca --show-hidden
```

### Usuwanie zadania
```sh
python todo.py remove <nazwa_listy> <numer_zadania>
```
Przykład:
```sh
python todo.py remove Praca 1
```

### Oznaczanie zadania jako ukończone
```sh
python todo.py complete <nazwa_listy> <numer_zadania>
```
Przykład:
```sh
python todo.py complete Praca 1
```

## Przechowywanie danych
Wszystkie listy zadań są zapisywane w jednym pliku `todo_lists.json`, co umożliwia ich trwałe przechowywanie między uruchomieniami programu.

## Uwagi
- Domyślnie ukończone zadania są ukrywane po 24 godzinach. Można je ponownie wyświetlić za pomocą `--show-hidden`.
- Jeśli plik `todo_lists.json` nie istnieje, zostanie utworzony automatycznie.

## Autor
Aplikacja stworzona w Pythonie jako prosty menedżer zadań działający w wierszu poleceń.

