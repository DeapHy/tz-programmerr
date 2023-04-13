import sys
from random import randint

class Task2:
    def __init__(self):

        # Параметры для случайной генерации
        self.__minPrice = 1         # Минимальная цена цыпленка
        self.__maxPrice = 10000     # Максимальная цена цыпленка
        self.__maxNominals = 10     # Максимальное количество номиналов
        self.__minNominal = 1       # Минимальное значение номинала
        self.__maxNominal = 100     # Максимальное значение номинала
        self.__price = 0            # Цена за цыпленка
        self.__offers = 0           # Количество предложений
        self.__data = list()

    # Определение возможности покупки цыпленка при заданных номиналах
    def isBuyable(self, nominals: list, target: int) -> bool:
        current = 0
        high = nominals[-1]
        low = nominals[0]
        for i in range(1, len(nominals)):
            current = 0
            while (current < target) and (current >= 0):
                if current + high > target:
                    for el in nominals:
                        if current + el == target:
                            return True
                current += high
            immutableCurrent = current
            for j in range(0, len(nominals)):
                current = immutableCurrent
                if i == j:
                    continue
                low = nominals[j]
                while (current >= target) and (current > 0):
                    if current == target:
                        return True
                    current = current - low if low > 0 else current + low
            high = nominals[-i-1]
        return False

    # Проверка данных
    def checkData(self, inp: str):
        self.__data = inp.split("\n")
        if len(self.__data[0].split(" ")) != 2:
            raise ValueError
        
        [self.__price, self.__offers] = [int(x) for x in self.__data[0].split(" ")]
        if self.__offers != len(self.__data[1::]):
            raise ValueError
    
    # Функция для получения из входных данных цены цыпленка и количества предложений, а также запуска функции find для каждого предложения
    def calculate(self, inp: str):
        self.checkData(inp)
        print(f"Начальные параметры:\nЦена = {self.__price}, Количество предложений = {self.__offers}\n===============")
        for i in range(self.__offers):
            nominals = [int(x) for x in self.__data[i+1].split(" ")]
            print(nominals)
            nominals.extend([-int(x) for x in self.__data[i+1].split(" ")])
            for i in range(len(nominals)):
                for j in range(len(nominals)):
                    if i != j and nominals[i] + nominals[j] != 0 and nominals[i] + nominals[j] not in nominals:
                        nominals.append(nominals[i] + nominals[j])
            nominals.sort()
            print("yes" if self.isBuyable(nominals, self.__price) else "no")

    # Функция для генерации теста (используется при запуске в режиме "Случайная генерация примера")
    def generateTest(self, count: int) -> str:
        output = f"{randint(self.__minPrice, self.__maxPrice)} {count}"
        for i in range(count):
            output += "\n"
            nominalsCount = randint(1, self.__maxNominals)
            testCase = []
            while len(testCase) < nominalsCount:
                nominal = randint(self.__minNominal, self.__maxNominal)
                if nominal not in testCase:
                    testCase.append(nominal) 
            output += " ".join([str(i) for i in testCase])
        return output

def main(argv: list):
    try:
        task = Task2()
        if "-r" in argv and not '-f' in argv:
            index = argv.index("-r")
            count = int(argv[index+1])
            inp = task.generateTest(count)
        elif "-f" in argv and not "-r" in argv:
            with open("testForTask2.txt", "r") as file:
                inp = file.read()
        else:
            raise AttributeError
        task.calculate(inp)
    except ValueError as exc:
        print("Неверный формат входных данных")
        return
    except Exception as e:
        print("\nДанный скрипт работает в двух режимах:\n\t- Случайная генерация примера (-r <число предложений>)\n\t- Чтение примера из файла (-f)\nПример случайной генерации: python3 task2.py -r 4\nПример чтения из файла: python3 task2.py -f\n")
        return

if __name__ == "__main__":
    main(sys.argv)