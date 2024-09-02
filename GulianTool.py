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


import os
import platform
import importlib


from program import Program
from typing import Dict

# Проверка установлен ли нужный модуль
try:
    importlib.import_module("requests")
    print(f"[log] Модуль requests установлен.")
except ImportError:
    print(f"[log] error - Модуль requests не установлен.")


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


    def show_logo(self) -> None:
        print(""+
"░██████╗░██╗░░░██╗██╗░░░░░██╗░█████╗░███╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░\n"
"██╔════╝░██║░░░██║██║░░░░░██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░\n"
"██║░░██╗░██║░░░██║██║░░░░░██║███████║██╔██╗██║░░░██║░░░██║░░██║██║░░██║██║░░░░░\n"
"██║░░╚██╗██║░░░██║██║░░░░░██║██╔══██║██║╚████║░░░██║░░░██║░░██║██║░░██║██║░░░░░\n"
"╚██████╔╝╚██████╔╝███████╗██║██║░░██║██║░╚███║░░░██║░░░╚█████╔╝╚█████╔╝███████╗\n"
"░╚═════╝░░╚═════╝░╚══════╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝\n")


    def show_menu(self) -> None:
        '''Выводит меню'''

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
    manager.show_logo()

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