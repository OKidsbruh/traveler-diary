# diary.py — Щоденник мандрівника

diary = [
    {"day": 1, "text": "Прибув до містечка Вербівка, зупинився на заїжджому дворі."},
    {"day": 2, "text": "Знайшов стару карту в руїнах на околиці міста."},
]


def print_diary(diary):
    """Виводить усі записи щоденника, відсортовані за номером дня."""
    print("=== Щоденник мандрівника ===")
    for entry in sorted(diary, key=lambda item: item["day"]):
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
    while True:
        day = get_int_input("Введи номер дня: ")
        if day > 0:
            break
        print("Помилка: номер дня має бути додатним числом.")

    while True:
        text = input("Введи текст запису: ").strip()
        if text:
            break
        print("Помилка: текст запису не може бути порожнім.")

    diary.append({"day": day, "text": text})
    print("Запис додано!")


def count_entries(diary):
    """Повертає загальну кількість записів у щоденнику."""
    return len(diary)


def entries_with_word(diary):
    """Виводить записи, які містять задане слово (без урахування регістру)."""
    word = input("Введи слово: ").strip()
    if not word:
        print("Пошук скасовано: слово не введено.")
        return

    print(f"Записи, які містять слово '{word}':")
    found = False
    needle = word.casefold()
    for entry in sorted(diary, key=lambda item: item["day"]):
        if needle in entry["text"].casefold():
            print(f"День {entry['day']}: {entry['text']}")
            found = True
    if not found:
        print("Нічого не знайдено.")


# Основна частина
print_diary(diary)
add_entry(diary)
print_diary(diary)
entries_with_word(diary)
print(f"Всього записів: {count_entries(diary)}")
