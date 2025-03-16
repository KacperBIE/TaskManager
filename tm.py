import argparse
import json
import os
import time

TODO_FILE = "zadania.json"
HIDE_AFTER = 604800  # Czas ukrycia w sekundach (domyślnie 7 dni)

def load_tasks():
    if os.path.exists(TODO_FILE) and os.path.getsize(TODO_FILE) > 0:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_tasks(zadania):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(zadania, file, indent=4)

def add_task(nazwa_listy, zadanie):
    zadania = load_tasks()
    if nazwa_listy not in zadania:
        zadania[nazwa_listy] = []
    zadania[nazwa_listy].append({"task": zadanie, "completed": False, "timestamp": time.time(), "hidden": False})
    save_tasks(zadania)
    print(f"Dodano zadanie do listy '{nazwa_listy}': {zadanie}")

def list_tasks(nazwa_listy, show_hidden=False):
    zadania = load_tasks()
    if nazwa_listy in zadania and zadania[nazwa_listy]:
        print(f"Lista zadań ({nazwa_listy}):")
        for i, zadanie in enumerate(zadania[nazwa_listy], 1):
            if not show_hidden and zadanie["completed"] and time.time() - zadanie["timestamp"] > HIDE_AFTER:
                zadanie["hidden"] = True
            if not zadanie["hidden"] or show_hidden:
                status = "[✔]" if zadanie["completed"] else "[ ]"
                print(f"{i}. {status} {zadanie['task']}")
    else:
        print(f"Brak zadań na liście '{nazwa_listy}'.")
    save_tasks(zadania)

def remove_task(nazwa_listy, numer_zadania):
    zadania = load_tasks()
    if nazwa_listy in zadania and 1 <= numer_zadania <= len(zadania[nazwa_listy]):
        usuniete_zadanie = zadania[nazwa_listy].pop(numer_zadania - 1)
        save_tasks(zadania)
        print(f"Usunięto zadanie z listy '{nazwa_listy}': {usuniete_zadanie['task']}")
    else:
        print("Nieprawidłowy numer zadania lub lista nie istnieje.")

def mark_task_completed(nazwa_listy, numer_zadania):
    zadania = load_tasks()
    if nazwa_listy in zadania and 1 <= numer_zadania <= len(zadania[nazwa_listy]):
        zadania[nazwa_listy][numer_zadania - 1]["completed"] = True
        zadania[nazwa_listy][numer_zadania - 1]["timestamp"] = time.time()
        save_tasks(zadania)
        print(f"Zadanie oznaczone jako ukończone na liście '{nazwa_listy}': {zadania[nazwa_listy][numer_zadania - 1]['task']}")
    else:
        print("Nieprawidłowy numer zadania lub lista nie istnieje.")

def main():
    parser = argparse.ArgumentParser(description="Lista TO-DO w Pythonie z obsługą wielu list")
    subparsers = parser.add_subparsers(dest="command", help="Dostępne polecenia")

    add_parser = subparsers.add_parser("dodaj", help="Dodaj zadanie (nazwa_listy zadanie)")
    add_parser.add_argument("nazwa_listy", type=str, help="Nazwa listy")
    add_parser.add_argument("zadanie", type=str, help="Treść zadania")

    list_parser = subparsers.add_parser("lista", help="Wyświetl listę zadań (nazwa_listy --pokaz-ukryte)")
    list_parser.add_argument("nazwa_listy", type=str, help="Nazwa listy")
    list_parser.add_argument("--pokaz-ukryte", action="store_true", help="Pokaż ukryte zadania")
    
    remove_parser = subparsers.add_parser("usun", help="Usuń zadanie (nazwa_listy numer_zadania)")
    remove_parser.add_argument("nazwa_listy", type=str, help="Nazwa listy")
    remove_parser.add_argument("numer_zadania", type=int, help="Numer zadania do usunięcia")

    complete_parser = subparsers.add_parser("ukoncz", help="Oznacz zadanie jako ukończone (nazwa_listy numer_zadania)")
    complete_parser.add_argument("nazwa_listy", type=str, help="Nazwa listy")
    complete_parser.add_argument("numer_zadania", type=int, help="Numer zadania do oznaczenia jako ukończone")

    args = parser.parse_args()
    
    if args.command == "dodaj":
        add_task(args.nazwa_listy, args.zadanie)
    elif args.command == "lista":
        list_tasks(args.nazwa_listy, args.pokaz_ukryte)
    elif args.command == "usun":
        remove_task(args.nazwa_listy, args.numer_zadania)
    elif args.command == "ukoncz":
        mark_task_completed(args.nazwa_listy, args.numer_zadania)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
