
def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
    return result


def seve_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list + '\n')
    return


def print_bus():
    return read_data_from_file('bus.txt')


def add_bus():
    id = 'bus' + str(int(print_bus()[len(print_bus())-1][0].strip('bus')) + 1)
    id_bus = id + ', ' + (input(f"Введите госномер автобуса {id}: "))
    seve_data_to_file('bus.txt', id_bus)
    return


def print_driver():
    return read_data_from_file('driver.txt')


def add_driver():
    id = 'driver' + \
        str(int(print_driver()[len(print_driver())-1][0].strip('driver')) + 1)
    id_driver = id + ', ' + (input(f"Введите фамилию водителя {id}: "))
    seve_data_to_file('driver.txt', id_driver)
    return


def print_route():
    return read_data_from_file('marshrut.txt')


def find(inList, fName):
    for i in inList:
        if i[0] == fName:
            return i[1]


def add_route():
    id = 'm' + str(int(print_route()[len(print_route())-1][0].strip('m')) + 1)
    id_route = id + ', ' + (input(f"Введите название маршрута {id}: "))
    print('Выберите автобус')
    n = 0
    route_data_bus = []
    list_bus = []
    list_all_bus = []
    for i in print_bus():
        list_bus.append(str(n))
        list_bus.append(i[0].strip(' '))
        list_bus.append(i[1].strip(' '))
        list_all_bus.append(list_bus)
        list_bus = []
        print(f'{n} ---{i[0]} -- {i[1]}')
        n += 1
    bus = input('Укажите номер автобуса в списке: ')
    for i in list_all_bus:
        if int(i[0]) == int(bus):
            route_data_bus.append(id_route + ', ' + i[1].strip(' '))
    print('Выберите водителя')
    n = 0
    route_data = []
    list_driver = []
    list_all_driver = []
    for i in print_driver():
        list_driver.append(str(n))
        list_driver.append(i[0].strip(' '))
        list_driver.append(i[1].strip(' '))
        list_all_driver.append(list_driver)
        list_driver = []
        print(f'{n} ---{i[0]} -- {i[1]}')
        n += 1
    driver = input('Укажите номер автобуса в списке: ')
    for i in list_all_driver:
        if int(i[0]) == int(driver):
            route_data.append(route_data_bus[0] + ', ' + i[1].strip(' '))
            print(f'Поздравляю запись "{route_data[0]}" сформирована')
    route = route_data[0]
    seve_data_to_file('marshrut.txt', route)

    return
