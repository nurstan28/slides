# Класс Абонент: Идентификационный номер, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Дебет, Кредит, Время междугородных и городских переговоров;
# Конструктор; Методы: установка значений атрибутов, получение значений атрибутов, вывод информации.
# Создать массив объектов данного класса. Вывести сведения относительно абонентов, у которых время городских переговоров превышает заданное.
# Сведения относительно абонентов, которые пользовались междугородной связью. Список абонентов в алфавитном порядке.

class Abonents:

    def __init__(self, identifier, surname, name, middle_name, adress, credit_card_number, debet, credit, time_intercity, time_city):
        self.identifier = identifier
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.adress = adress
        self.credit_card_number = credit_card_number
        self.debet = debet
        self.credit = credit
        self.time_city = time_city
        self.time_intercity = time_intercity

        self.get_atributes()

    def get_atributes(self):
        # установка значения атрибутов и получение значений атрибутов

        self.identifier = input("Введите ID: ")
        self.surname = input("Введите Фамилию: ")
        self.name = input("Введите Имя: ")
        self.middle_name = input("Введите Отчество: ")
        self.adress = input("Введите Адресс: ")
        self.credit_card_number = input("Номер кредитной карты: ")
        self.debet = input("Введите Дебет: ")
        self.credit = input("Введите Кредит: ")
        self.time_city = input("Введите время городских переговоров.\nВремя переговоров: ")

        self.time_intercity = input("Введите время междугородных переговоров, по примеру: 1:30, если их не было напишите \"Нет\"\nВремя переговоров: ")

    def person_time(self):
        return self.time_intercity

    def info(self):
        # вывод информации
        print("ID: "+str(self.identifier), "\nФамилия: "+str(self.surname), "\nИмя: "+str(self.name), "\nОтчество: "+str(self.middle_name),
            "\nАдресс: "+str(self.adress), "\nНомер кредитной карточки: "+str(self.credit_card_number), "\nДебит: "+str(self.debet),
            "\nКредит: "+str(self.credit), "\nВремя междугородных переговоров: "+str(self.time_intercity), "\nВремя городских переговоров: "+str(self.time_city))



    def str_to_time(self):
        # Вводим строку, получаем время
        if self.time_intercity == "Нет":
            return self.time_intercity
        str_date = self.time_intercity.split(":")
        str_date = str_date[0]
        return int(str_date)





def main():
    all_obj = []
    obj1 = Abonents("1281002", "Smitt", "Will", "Carroll", "New-York", "378282246310005", "400", "0", "1:10", "0:05")
    all_obj.append(obj1)
    obj2 = Abonents("1218492", "Ronaldo", "Cristiano", "dos Santos Aveiro", "Manchester", "37223246310045", "200", "0", "0:45", "0:35")
    all_obj.append(obj2)
    obj3 = Abonents("1218492", "Messi", "Leonel", "Андре́с", "Paris", "37223246310045", "400", "0", "1:00", "0:55")
    all_obj.append(obj3)

    # Выводим справку, если время переговоров превышает время лимита
    for obj in all_obj:
        try:
            user_time = obj.str_to_time()
            # 1 - это один час
            if user_time == "Нет":
                pass
            elif 0 <= user_time < 1:
                obj.info()
                print("*Данный пользователь пользовался междугородной связью*\n")
            elif user_time >= 1:
                obj.info()
                print("*Данный пользователь пользовался междугородной связью*")
                print("**Пользователю выдана справка о том, что время междугородных переговоров превысило время лимита**\n")
        except:
            print("\nПользователь указал время не правильно!")

if __name__ == '__main__':
    main()