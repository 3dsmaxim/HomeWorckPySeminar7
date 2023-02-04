
import function as fn



menuitems = [
    ("1", "Вывод Автобусов", fn.print_bus),
    ("2", "Добавление автобуса", fn.add_bus),
    ("3", "Вывод водителей", fn.print_driver),
    ("4", "Добовление водителе", fn.add_driver),
    ("5", "Вывод маршрута", fn.print_route,),
    ("6", "Добовление маршрута", fn.add_route),
    ("7", "Выход", lambda: exit())
]

for i in menuitems:
    print(i[0], i[1])
text = input("Выберете действие ")
if text == '1':
    for i in fn.print_bus():
        print(f'{i[0]} -- {i[1]}')
elif text == '2':
    fn.add_bus()
elif text == '3':
    for i in fn.print_driver():
        print(f'{i[0]} -- {i[1]}')
elif text == '4':
    fn.add_driver()
elif text == '5':

    for i in fn.print_route():
        print(
            f"{i[0].strip(' ')} - {i[1].strip(' ')} -- {fn.find(fn.print_bus(), i[2].strip(' ')).strip(' ')} - {fn.find(fn.print_driver(), i[3].strip(' ')).strip(' ')}")
elif text == '6':
    fn.add_route()
elif text == '7':
    exit()
