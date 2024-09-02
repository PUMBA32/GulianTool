import random
import platform
import requests
import datetime

from generator import Generator
from typing import Dict


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