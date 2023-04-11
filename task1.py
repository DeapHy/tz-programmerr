import sys
from random import randint

# Параметры для случайной генерации
minCityCount = 1     # Минимальное количество городов
maxCityCount = 100   # Максимальное количество городов
minRoadsCount = 1    # Минимальное количество дорог
maxRoadsCount = 100  # Максимальное количество дорог

# Класс город, храняций информацию о конкретном городе
class City:
    def __init__(self, ind: int):
        self.cityIndex = ind                # Индекс города
        self.connections = list()           # Индексы других городов с которыми соединенен текущий город

    # Красивый вывод информации о городе
    def __repr__(self) -> str:
        return f"Город {self.cityIndex}"

    # Добавление дороги в другой город
    def addConnection(self, ind: int) -> None:
        self.connections.append(ind)

    # Получение всех дорог, с которым соединенен данный город
    def getConnections(self) -> list:
        return self.connections
    
# Класс штат, хранящий информацию о конкретном штате
class State:
    def __init__(self):
        self.cities = list()        # Города, которые входят в штат

    # Вывод содержимого штата (городов, входящих в этот штат, по большей части для тестов)
    def __repr__(self) -> str:
        return f"{self.cities}"

    # Получение списка городов, входящих в данный штат
    def getCities(self) -> list:
        return self.cities
    
    # Добавление нового города в штат
    def addCity(self, cty: City) -> None:
        self.cities.append(cty)

# Основной класс программы
class Task1:
    def __init__(self, inp: str) -> None:
        tempData = inp.split("\n")
        self.cityCount, self.roadCount = [int(x) for x in tempData[0].split(" ")]   # Загрузка основной информации
        self.roads = [[int(y) for y in x.split(" ")] for x in tempData[1::]]        # Загрузка списка всех дорог
        self.cities = [City(i) for i in range(self.cityCount)]                      # Создание объектов под каждый город
        self.states = list()                                                        # Создание пустого списка штатов

    # Соединение городов дорогами
    def connectCities(self) -> None:
        for road in self.roads:  
            self.cities[road[0]].addConnection(road[1])         # Двустороннее объединение городов                       
            self.cities[road[1]].addConnection(road[0])         # Двустороннее объединение городов

    # Выполнение задания
    def run(self) -> int:
        self.connectCities()                            # Загрузка всех дорог
        state = State()                                 # По крайней мере должен существовать 1 штат
        state.addCity(self.cities[0])                   # С 1 городом в нем
        self.states.append(state)                       # Штат добавляется в общий список штатов
        for i in range(1, self.cityCount):              # Для каждого города кроме первого
            flag = False                                # Сброс флага
            for state in self.states:                   # Для каждого штата
                for city in state.getCities():          # Для каждого города в штате
                    if i in city.getConnections():      # Если индекс города присутствует в любом городе штата (в этот город есть дорога)
                        state.addCity(self.cities[i])   # Город добавляется в данный штат
                        flag = True                     # Устанавливаем, что город добавился в какой-либо штат
                        break                           # Выход из цикла по городам штата
                    if flag:                            # Если город добавился в какой-либо штат, то нет необходимости смотреть другие штаты
                        break                           # Выход из цикла по штатам
            if not flag:                                # Если гроод никуда не добавился
                state = State()                         # Создается новый штат
                state.addCity(self.cities[i])           # Куда добавляется этот город
                self.states.append(state)               # Штат добавляется в список штатов

        return len(self.states)                         # Длина списка штатов является ответом
    
def generateTest():
    roadCount = randint(minRoadsCount, maxRoadsCount)
    cityCount = randint(minCityCount, maxCityCount)
    output = f"{cityCount} {roadCount}"
    for i in range(roadCount):
        output += "\n"
        temp = [int(randint(0, cityCount-1)) for x in range(2)]

        output += " ".join([str(i) for i in temp])
    print(output)
    return output


def main(argv: list):
    try:
        if "-r" in argv and not '-f' in argv:
            inp = generateTest()
        elif "-f" in argv and not "-r" in argv:
            with open("testForTask1.txt", "r") as file:
                inp = file.read()
        else:
            raise ValueError
        task = Task1(inp)
        print(task.run())
    except Exception as e:
        print(e.with_traceback())
        print("\nДанный скрипт работает в двух режимах:\n\t- Случайная генерация примера (-r)\n\t- Чтение примера из файла (-f)\nПример случайной генерации: python3 task1.py -r\nПример чтения из файла: python3 task1.py -f\n")
        return

if __name__ == "__main__":
    main(sys.argv)
# if __name__ == "__main__":
#     inp = """6 4
# 3 1
# 1 2
# 5 4
# 2 3"""
#     t = Task1(inp)
#     t.run()