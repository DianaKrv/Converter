



def convertToRu():
    convertation = int(input('Что считаем: \n 1. Температура\n 2. Вес\n 3. Длина\n 4. Объем\n 5. Скорость\n '))
    #print(convertation)


def convertToEng():
    print('Конвертация из неметрической в метрическую')
    convertation = int(input('Что считаем: \n 1. Температура\n 2. Вес\n 3. Длина\n 4. Объем\n 5. Скорость\n '))
    #print(convertation)






var = int(input('1: Ru - Eng\n2: Eng - Ru\n'))

def choice(var):
    if var == 1:
        #print("Выбрано 1: Ru")
        convertToRu()
    elif var == 2:
        #print("Выбрано 2: Eng")
        convertToEng()