import sys
from random import randint

class Task1():
    def __init__(self):

        # Параметры для случайной генерации
        self.__minPrice = 1         # Минимальная цена цыпленка
        self.__maxPrice = 10000     # Максимальная цена цыпленка
        self.__maxNominals = 10     # Максимальное количество номиналов
        self.__minNominal = 1       # Минимальное значение номинала
        self.__maxNominal = 100     # Максимальное значение номинала

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

    # Функция для получения из входных данных цены цыпленка и количества предложений, а также запуска функции find для каждого предложения
    def calculate(self, inp: str):
        data = inp.split("\n")
        [price, n] = [int(x) for x in data[0].split(" ")]
        print(f"Начальные параметры:\nЦена = {price}, Количество предложений = {n}\n===============")
        for i in range(n):
            nominals = [int(x) for x in data[i+1].split(" ")]
            print(nominals)
            nominals.extend([-int(x) for x in data[i+1].split(" ")])
            for i in range(len(nominals)):
                for j in range(len(nominals)):
                    if i != j and nominals[i] + nominals[j] != 0 and nominals[i] + nominals[j] not in nominals:
                        nominals.append(nominals[i] + nominals[j])
            nominals.sort()
            print("yes" if self.isBuyable(nominals, price) else "no")

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
        task = Task1()
        if "-r" in argv and not '-f' in argv:
            index = argv.index("-r")
            count = int(argv[index+1])
            inp = task.generateTest(count)
        elif "-f" in argv and not "-r" in argv:
            with open("testForTask1.txt", "r") as file:
                inp = file.read()
        else:
            raise ValueError
        task.calculate(inp)
    except Exception as e:
        print("\nДанный скрипт работает в двух режимах:\n\t- Случайная генерация примера (-r <число предложений>)\n\t- Чтение примера из файла (-f)\nПример случайной генерации: python3 t.py -r 4\nПример чтения из файла: python3 t.py -f\n")
        return

if __name__ == "__main__":
    main(sys.argv)