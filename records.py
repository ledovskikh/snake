import csv


def load_records(filename="records.csv"):
    try:
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            records = []
            for row in reader:
                try:
                    row["score"] = int(
                        row["score"]
                    )  # Преобразуем счёт в int, если это возможно
                    records.append(row)
                except (
                    ValueError,
                    KeyError,
                ):  # Пропускаем строки с некорректными данными
                    continue
            return sorted(records, key=lambda x: x["score"], reverse=True)
    except FileNotFoundError:
        return []


def save_record(username, score, filename="records.csv"):
    """Добавляет новую запись рекорда в файл."""
    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, score])
