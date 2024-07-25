import argparse
from dataclasses import dataclass

file_path = "books.txt"
# python main.py add --buyer "козлов" --title "сахар" --kolichestvo "30.88848888" --cena "10"


@dataclass
class tovar_pos:

    def __init__(self, buyer, title, kolichestvo, cena):
        self.buyer = buyer
        self.title = title
        self.kolichestvo = kolichestvo
        self.cena = cena


class detalization:
    def __init__(self):
        self.tovar_pos = []

    def add_user(self, buyer, title, kolichestvo, cena):
        with open(file_path, "a") as file:
            tovar = tovar_pos(title, cena, buyer, kolichestvo)
            self.tovar_pos.append(tovar)
            okruglenie = round(float(cena) * float(kolichestvo), 2)
            summa = round(kolichestvo * cena)
            rashozdenie = round(summa - okruglenie, 8)
            file.write(title + "|" + buyer + "|" + str(kolichestvo) + "|"
                       + str(okruglenie) + "|" + str(rashozdenie) + "|" + str(summa) + "\n")
            print("покупатель" + " '" + buyer + "' " + "успешно добавлена в накладную.")


if __name__ == "__main__":
    detalization = detalization()

    parser = argparse.ArgumentParser(description="Управление библиотекой накладных")
    parser.add_argument("action", choices=["add"], help="Действие")
    parser.add_argument("--title", help="Название товара")
    parser.add_argument("--buyer", help="Автор книги")
    parser.add_argument("--cena", type=float, help="Год издания")
    parser.add_argument("--kolichestvo", type=float, help="Статус книги")

    args = parser.parse_args()
    if args.action == "add":
        detalization.add_user(args.title, args.buyer, args.kolichestvo, args.cena)
