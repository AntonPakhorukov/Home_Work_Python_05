# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Задача 2: Создайте программу для игры в ""Крестики-нолики"".

# Задача 3: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

try:
    task = int(input('Введите номер задачи: '))
except ValueError:
    print('Не корректный ввод')
    raise SystemExit
match task:
    case 1:
        with open('Text.txt', 'w+', encoding='utf=8') as data:
            data.write(input('Введите преджложение: '))
            data.seek(0, 0)
            string = data.read()
        result = list(filter(lambda x: 'абв' not in x and 'а' not in x and 'б' not in x and 'в' not in x                                         
                                        and 'аб' not in x and 'бв' not in x and 'ба' not in x and 'вб' not in x                                    
                                        and 'ав' not in x and 'ва' not in x, string.split()))
        print(f'Введенная строка: {string}')
        print(f'Вывод: ', end='')
        print(*result)
    case 2:
        def table(list):
            print('-------------')
            print('|', list[0], '|', list[1], '|', list[2], '|')
            print('|', list[3], '|', list[4], '|', list[5], '|')
            print('|', list[6], '|', list[7], '|', list[8], '|')
            print('-------------')
        start = list(range(1, 10))
        table(start)
        def input_el():
            while True:
                a = input('Введите знак (x/o): ')
                if not a in 'xo':
                    print('Не вверный ввод знака')
                    table(start)
                    continue
                try:
                    b = int(input(f'Введите номер ячейки для {a}: '))
                except ValueError:
                    print('Такой ячейки нет')
                    table(start)
                    continue
                if b < 1:
                    print('Такой ячейки нет')
                    table(start)
                    continue
                elif b > 9:
                    print('Такой ячейки нет')
                    table(start)
                    continue
                if str(start[b - 1]) in 'xo':
                    print('Ячейка занята, выберите другую')
                    table(start)
                    continue
                else:
                    start[b - 1] = a
                    break
        input_el()
        count = 1
        table(start)
        for i in range(len(start)):
            if (start[0]) == (start[1]) == (start[2]):
                print(f'Win {str(start[0])}')
                break
            elif (start[3]) == (start[4]) == (start[5]):
                print(f'Win {str(start[4])}')
                break   
            elif (start[6]) == (start[7]) == (start[8]):
                print(f'Win {str(start[7])}')
                break 
            elif (start[0]) == (start[3]) == (start[6]):
                print(f'Win {str(start[3])}')
                break
            elif (start[1]) == (start[4]) == (start[7]):
                print(f'Win {str(start[4])}')
                break   
            elif (start[2]) == (start[5]) == (start[8]):
                print(f'Win {str(start[5])}')
                break   
            elif (start[0]) == (start[4]) == (start[8]):
                print(f'Win {str(start[4])}')
                break   
            elif (start[2]) == (start[4]) == (start[6]):
                print(f'Win {str(start[2])}')
                break 
            else:
                input_el()
                table(start)
                count = count + 1
                if count == 9:
                    print('Ничья, победила дружба!')
                    break
    case 3:
        with open('Task03.txt', 'r', encoding='utf-8') as text:
            first_str = text.readline()
            str_out = ''
            index = 0
            count = 1
            while index < len(first_str) - 1:
                if first_str[index] == first_str[index + 1]:
                    count += 1
                    if index == len(first_str) - 2:
                        str_out += str(count) + first_str[index]
                else:
                    if count == 1:
                        str_out = str_out + str(count) + first_str[index]
                        if index == len(first_str) - 2:
                            if first_str[index] != first_str[index + 1]:
                                str_out += str(count) + first_str[index + 1]
                    else:
                        str_out += str(count) + first_str[index]
                    count = 1
                index += 1    
        print(first_str)
        print(str_out)
        with open('Code.txt', 'w', encoding='utf-8') as code:
            code.write(str_out)
        with open('Code.txt', 'r', encoding='utf-8') as wcode:
            coding = wcode.readline()
        with open('Write.txt', 'w', encoding='utf-8') as data:
            result = ''
            for i in range(0, (len(str_out) - 1), 2):
                result += coding[i + 1] * int(coding[i])
            data.write(result)
        print(coding)
        print(result)

