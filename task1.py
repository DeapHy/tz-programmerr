import sys
from random import randint

minPrice = 1
maxPrice = 10000
maxNominals = 10
minNominal = 1
maxNominal = 100

def find(nominals: list, target: int):
    current = 0
    high = nominals[-1]
    low = nominals[0]
    for i in range(1, len(nominals)):
        current = 0
        while (current < target) and (current >= 0):
            if current + high > target:
                for el in nominals:
                    if current + el == target:
                        print("yes")
                        return
            current += high
        immutableCurrent = current
        for j in range(0, len(nominals)):
            current = immutableCurrent
            if i == j:
                continue
            low = nominals[j]
            while (current >= target) and (current > 0):
                if current == target:
                    print("yes")
                    return
                current = current - low if low > 0 else current + low
        high = nominals[-i-1]
    print("no")

def calculate(inp: str):
    data = inp.split("\n")
    [price, n] = [int(x) for x in data[0].split(" ")]
    print(f"Начальные параметры:\nЦена = {price}, Количество предложений = {n}\n===============")
    for i in range(n):
        nominals = [int(x) for x in data[i+1].split(" ")]
        print(nominals)
        nominals.extend([-int(x) for x in data[i+1].split(" ")])
        nominals.sort()
        find(nominals, price)

def generateTest(count: int) -> str:
    output = f"{randint(minPrice, maxPrice)} {count}"
    for i in range(count):
        output += "\n"
        nominalsCount = randint(1, maxNominals)
        testCase = [randint(minNominal, maxNominal) for i in range(nominalsCount)]
        output += " ".join([str(i) for i in testCase])
    return output

def main(argv: list):
    try:
        if "-r" in argv and not '-f' in argv:
            index = argv.index("-r")
            count = int(argv[index+1])
            print(count)
            inp = generateTest(count)
        elif "-f" in argv and not "-r" in argv:
            with open("test.txt", "r") as file:
                inp = file.read()
        else:
            raise ValueError
        calculate(inp)
    except:
        print("\nДанный скрипт работает в двух режимах:\n\t- Случайная генерация примера (-r <число предложений>)\n\t- Чтение примера из файла (-f)\nПример случайной генерации: python3 t.py -r 4\nПример чтения из файла: python3 t.py -f\n")
        return

if __name__ == "__main__":
    main(sys.argv)