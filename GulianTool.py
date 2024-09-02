'''
+------------------------------+
| [1] - случайны пароль        |
| [2] - сгенерировать личность |
| [3] - информация о системе   |
| [4] - информация о сайте     |
| [5] - выбор языка            |
| [6] - выход                  |
+------------------------------+

'''




import random
import os
import platform
import requests
import datetime
import socket

from typing import List, Tuple, Dict



class Generator:
    @staticmethod
    def f_name(g: str) -> str:
        '''Генерация случайного русского имени'''

        m_f_names: List[str] = [
            "Александр", "Алексей", "Андрей", "Антон", "Артем",
            "Борис", "Вадим", "Валерий", "Василий", "Виктор",
            "Виталий", "Владимир", "Владислав", "Вячеслав", "Геннадий",
            "Георгий", "Григорий", "Денис", "Дмитрий", "Евгений",
            "Иван", "Игорь", "Кирилл", "Константин", "Леонид",
            "Максим", "Михаил", "Николай", "Олег", "Павел"
        ]
        w_f_names: List[str] = [
            "Александра", "Алена", "Алина", "Алиса", "Алла",
            "Анастасия", "Анна", "Антонина", "Валентина", "Валерия",
            "Варвара", "Вера", "Вероника", "Виктория", "Галина",
            "Дарья", "Евгения", "Екатерина", "Елена", "Елизавета",
            "Инна", "Ирина", "Кира", "Кристина", "Лариса",
            "Людмила", "Мария", "Маргарита", "Наталья", "Ольга"
        ]
        return random.choice(m_f_names) if g[0] == 'м' else random.choice(w_f_names)


    @staticmethod
    def s_name(g: str) -> str:
        '''Генерация случайной русской фамилии'''

        s_names: List[str] = [
            "Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев",
            "Петров", "Соколов", "Михайлов", "Федоров", "Морозов",
            "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров",
            "Павлов", "Степанов", "Смирнов", "Сергеев", "Кузьмин",
            "Захаров", "Зайцев", "Соловьев", "Борисов", "Яковлев",
            "Романов", "Виноградов", "Соболев", "Сергеев", "Родионов"
        ]
        result: str = random.choice(s_names)
        return result if g[0] == 'м' else result+'а'
    

    @staticmethod
    def t_name(g: str) -> str:
        '''Генерации случайного русского общества'''

        m_f_names = [
            "Александрович", "Алексеевич", "Андреевич", "Антонович", "Артемович",
            "Борисович", "Вадимович", "Валерьевич", "Васильевич", "Викторович",
            "Витальевич", "Владимирович", "Владиславович", "Вячеславович", "Геннадьевич",
            "Георгиевич", "Григорьевич", "Денисович", "Дмитриевич", "Евгеньевич",
            "Иванович", "Игоревич", "Кириллович", "Константинович", "Леонидович",
            "Максимович", "Михайлович", "Николаевич", "Олегович", "Павлович"
        ]
        w_f_names = [
            "Александровна", "Алексеевна", "Андреевна", "Антоновна", "Артемовна",
            "Борисовна", "Вадимовна", "Валерьевна", "Васильевна", "Викторовна",
            "Витальевна", "Владимировна", "Владиславовна", "Вячеславовна", "Геннадьевна",
            "Георгиевна", "Григорьевна", "Денисовна", "Дмитриевна", "Евгеньевна",
            "Ивановна", "Игоревна", "Кирилловна", "Константиновна", "Леонидовна",
            "Максимовна", "Михайловна", "Николаевна", "Олеговна", "Павловна"
        ]
        return random.choice(m_f_names) if g[0] == 'м' else random.choice(w_f_names)

    
    @staticmethod
    def phone_number() -> str:
        '''Генерация случайного номера телефона'''

        number: str = "+7"
        for i in range(10):
            number += str(random.randint(0,9))
        return number


    @staticmethod
    def town() -> str:
        '''Генерации случайного Российского города'''

        towns: List[str] = [
            "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
            "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону",
            "Уфа", "Красноярск", "Воронеж", "Пермь", "Волгоград",
            "Краснодар", "Саратов", "Тюмень", "Тольятти", "Ижевск"
        ]
        return random.choice(towns)


    @staticmethod
    def password(length: int) -> str:
        '''Генерация случайного пароля указанной длины'''

        letters: str = "qwertyuioplkjhgfdsazxcvbnm"
        numbers: str = "1234567890"
        symbols: str = "_-"
        result: List[str] = []

        for _ in range(length):
            r_n: int = random.randint(1,10)
            if r_n > 0 and r_n <= 6: 
                l = random.choice(letters)
                if random.randint(0,1) == 0: l = l.upper()
                result.append(l)
            elif r_n > 6 and r_n <= 9: 
                result.append(random.choice(numbers))
            else: 
                result.append(random.choice(symbols))
        
        return "".join(result)
    

    @staticmethod
    def hosting_info(domain: str) -> Dict[str, str]:
        '''Получение информации о сайте по его домену (ip, hostname, city, country, location, provider)'''

        try:
            ip: str = socket.gethostbyname(domain)
        except socket.gaierror:
            return {"data": "ошибка поиска"}
        
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            site_info = {
                "домен": domain,
                "IP": data.get("ip"),
                "имя хоста": data.get("hostname"),
                "город": data.get("city"),
                "регион": data.get("region"),
                "страна": data.get("country"),
                "локация": data.get("loc"),
                "провайдер": data.get("org")
            }
            return site_info
        else:
            return {"data": "ошибка поиска"}



class Program:
    def __init__(self) -> None:
        pass


    def __get_ip(self) -> str:
        '''Получение айпишника текущего ПК'''

        try:
            response = requests.get('https://api.ipify.org?format=json')
            ip_data = response.json()
        except:
            return "none"
        else:
            return ip_data['ip']
    

    def get_sys_info(self) -> Dict[str, str]:
        '''Возвращает информацию о текущем ПК (OS, data, time, ip)'''

        info: Dict[str, str] = {}
        info['OS'] = platform.system()
        info['дата'] = datetime.datetime.now().strftime("%Y-%m-%d")
        info['время'] = str(datetime.datetime.now().time())[:-7]
        info['IP'] = self.__get_ip()
        return info


    def show_dict(self, dict: Dict[str, str]) -> None:
        '''Выводит словарь'''

        for key, value in dict.items():
            print(f'[>] {key} - {value}')
        print()

    
    def get_random_password(self, length: int) -> str:
        '''Возвращает случайный пароль'''

        return Generator.password(length)

    
    def generate_person(self, gender: str, old: str) -> Dict[str, str]:
        '''Генерация случайного человека (информации о нем)'''

        person: Dict[str, str] = {}

        person['пол'] = "мужчина" if gender == 'м' else "женщина"
        
        age: int = 0
        if old == '1': age += random.randint(5, 18)
        elif old == '2': age += random.randint(19, 35)
        else: age += random.randint (36, 60)
        
        person['возраст'] = str(age)
        person['имя'] = f"{Generator.f_name(gender)} {Generator.s_name(gender)} {Generator.t_name(gender)}"
        person['номер телефона'] = Generator.phone_number()
        person['страна'] = 'Россия'
        person['город'] = Generator.town()
    
        return person
    

    def get_info_by_domain(self, domain: str) -> None:     
        '''Возвращает информацию о сайте по домену'''

        return Generator.hosting_info(domain)



class ConsoleManager:
    def __init__(self) -> None:
        self.menu = (
            'случайны пароль',
            'сгенерировать личность',
            'информация о системе',
            'информация о сайте',
            'выбор языка',
            'выход'
        )
        

    def clear_console(self) -> None:
        '''Чистит консоль'''

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


    def show_menu(self) -> None:
        '''Выводит меню'''

        print(""+
"░██████╗░██╗░░░██╗██╗░░░░░██╗░█████╗░███╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░\n"
"██╔════╝░██║░░░██║██║░░░░░██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░\n"
"██║░░██╗░██║░░░██║██║░░░░░██║███████║██╔██╗██║░░░██║░░░██║░░██║██║░░██║██║░░░░░\n"
"██║░░╚██╗██║░░░██║██║░░░░░██║██╔══██║██║╚████║░░░██║░░░██║░░██║██║░░██║██║░░░░░\n"
"╚██████╔╝╚██████╔╝███████╗██║██║░░██║██║░╚███║░░░██║░░░╚█████╔╝╚█████╔╝███████╗\n"
"░╚═════╝░░╚═════╝░╚══════╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝\n")

        COUNT: int = 30
        print("+", end="")
        print("-"*COUNT+"+")
        for i, el in enumerate(self.menu):
            tabs: int = 30 - (7 + len(el)) 
            print(f'| [{i+1}] - {el}' + (" "*tabs) +'|')
        print("+", end="")
        print("-"*COUNT+"+")



def main() -> None:
    program = Program()
    manager = ConsoleManager()

    manager.clear_console()
    while True:
        manager.show_menu()

        inp: str = input(">>> ").strip()

        manager.clear_console()
        match inp:
            case "1":
                try:
                    length: str = int(input("длина пароля: "))
                except:
                    print("[!] ошибка, ты должен ввести число")
                password: str = program.get_random_password(length)

                manager.clear_console()
                print(f"[+] ваш пароль: {password}\n")
            case "2": 
                gender = input("пол (м/ж) по стандарту 'м': ").strip().lower()
                old = input("возраст \n[1] - ребенок\n[2] - взрослый\n[3] - пожилой\nпо стандарту 'взрослый': ").strip().lower()

                person: Dict[str, str] = program.generate_person(gender, old)
                
                manager.clear_console()
                print("[+] Ваша новая личность:\n")
                program.show_dict(person)
            case "3":
                manager.clear_console()
                print("[+] Информация по текущей системе")
                program.show_dict(program.get_sys_info())
            case "4":
                domain: str = input("введите домен сайта: ")
                info: Dict[str, str] = program.get_info_by_domain(domain)

                manager.clear_console()
                print(f"[+] Информация по домену {domain}\n")
                program.show_dict(info)
            case "5":
                select: str = input("Выберите язык (ru/en): ").strip().lower()
                
            case _:
                break
        

if __name__ == '__main__':
    main()