# diary.py — Щоденник мандрівника

diary = [
    {"day": 1, "text": "Прибув до містечка Вербівка, зупинився на заїжджому дворі."},
    {"day": 2, "text": "Знайшов стару карту в руїнах на околиці міста."},
]

def print_diary(diary):
    """Виводить усі записи щоденника."""
    print("=== Щоденник мандрівника ===")
    for entry in diary:
        print(f"День {entry['day']}: {entry['text']}")
    print()

def get_int_input(prompt):
    """Безпечне введення цілого числа (з повторним запитом при помилці)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка: введи ціле число.")

def add_entry(diary):
    """Запитує номер дня і текст нового запису та додає його до щоденника."""
    day = get_int_input("Введи номер дня: ")
    text = input("Введи текст запису: ")
    diary.append({"day": day, "text": text})
    print("Запис додано!")

def count_entries(diary):
    """Повертає загальну кількість записів у щоденнику."""
    return len(diary)

# Основна частина
print_diary(diary)
add_entry(diary)
print_diary(diary)
print(f"Всього записів: {count_entries(diary)}")