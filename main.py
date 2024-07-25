import argparse
from dataclasses import dataclass

file_path = "books.txt"
#создаём в репозитории новый файл с названием books.txt

#создаём  класс tovar_pos, который представляет товар в покупке.
#У класса есть четыре атрибута: buyer, title, kolichestvo и cena, которые хранят информацию о покупателе, наименовании товара, количестве товара и цене соответственно.
@dataclass
class tovar_pos:

    def __init__(self, buyer, title, kolichestvo, cena):
        self.buyer = buyer
        self.title = title
        self.kolichestvo = kolichestvo
        self.cena = cena


class detalization:
    def __init__(self):
       # инициализируем атрибут tovar_pos пустым списком. 
        self.tovar_pos = []
# Функция,добавляет необходимую информацию в файл.Функция принимает параметры, такие как покупатель (buyer), название товара (title), количество (kolichestvo) и цена (cena).
    def add_user(self, buyer, title, kolichestvo, cena):
        #дальше часть кода открывает файл с разрешением только на read+add,так же указывается параметры,которые и будут добавлены в файл
        with open(file_path, "a") as file:
            tovar = tovar_pos(title, cena, buyer, kolichestvo)
            self.tovar_pos.append(tovar)
            #вычесление необходимых переменных(round-указывает на 2 показателя(вычесления,сколько чисел после запятых не округлять))
            okruglenie = round(float(cena) * float(kolichestvo), 2)
            summa = round(kolichestvo * cena)
            rashozdenie = round(summa - okruglenie, 8)
            #запись в файл
            file.write(title + "|" + buyer + "|" + str(kolichestvo) + "|" + str(okruglenie) + "|" + str(rashozdenie) + "|" + str(summa) + "\n")

#функция запуска класса
if __name__ == "__main__":
    detalization = detalization()
#инициализируют парсер аргументов argparse.ArgumentParser с описанием, действием и возможными аргументами:
#   - Действие (action): обязательный аргумент, принимающий только значение "add".
#  - Дополнительные аргументы: "--title", "--buyer", "--cena", "--kolichestvo", предназначенные для имени покупателя, названия товара, цены и количества в килограммах соответственно.
    parser = argparse.ArgumentParser(description="Управление библиотекой накладных")
    parser.add_argument("action", choices=["add"], help="Действие")
    parser.add_argument("--title", help="имя покупателя")
    parser.add_argument("--buyer", help="название товара")
    parser.add_argument("--cena", type=float, help="цена")
    parser.add_argument("--kolichestvo", type=float, help="количество в  кг")
    
#Аргументы командной строки парсятся с помощью args = parser.parse_args(), и их значения присваиваются переменным args.title, args.buyer, args.cena, args.kolichestvo.
    args = parser.parse_args()

#Далее, происходит проверка значения args.action: если оно равно "add",
#то вызывается функция detalization.add_user(args.title, args.buyer, args.kolichestvo, args.cena), которая добавляет данные о пользователе в библиотеку накладных.    
    
    if args.action == "add":
        detalization.add_user(args.title, args.buyer, args.kolichestvo, args.cena)
