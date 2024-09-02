import random
import requests
import socket

from typing import List, Dict


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