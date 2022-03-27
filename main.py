import random
from Data import data_base, data_base_standart


randchoise = random.choice(data_base['abc_and_numbers'])
a = 'a'


def ciphering():
    text = input('Введите текст: ')
    new_text = ''
    sepor_text = list(text)
    for l in sepor_text:
        for i in data_base['shifr'].keys():
            if i == l:
                new_text = new_text + data_base['shifr'][i] + 'a'
    print(new_text)
    cipher_file = open('cipher_text.txt', 'w+')
    cipher_file.write(new_text)


def deciphering():
    text = input('Введите текст: ')
    new_text = ''
    decipher_text = text.split('a')
    for l in decipher_text:
        for i, o in data_base['shifr'].items():
            if o == l:
                new_text = new_text + i
    print(new_text)
    decipher_file = open('decipher_text.txt', 'w+')
    decipher_file.write(new_text)
    decipher_file.close()


def clear():
    decipher_file = open('decipher_text.txt', 'w+')
    decipher_file.write(' ')
    decipher_file.close()
    cipher_file = open('cipher_text.txt', 'w+')
    cipher_file.write(' ')
    cipher_file.close()


def cipher_main_menu():
    while True:
        print(' ')
        print('*** Меню ***')
        print('1. Шифрация')
        print('2. Дешифрация')
        print('3. Очистка кэша')
        print('4. Генерация новых ключей')
        print('5. Сброс до стандартных ключей')
        print('6. Импорт ключей')
        print('7. Экспорт ключей')
        print('0. Выход')
        choise = input('Выберите действие: ')
        if choise == '1':
            ciphering()
        elif choise == '2':
            deciphering()
        elif choise == '3':
            clear()
        elif choise == '4':
            random_keys_generation()
        elif choise == '5':
            standart_keys()
        elif choise == '6':
            import_cipher()
            print(data_base['shifr'])
        elif choise == '7':
            export_cipher()
            print(data_base['shifr'])
        elif choise == '0':
            exit(0)
        else:
            print('Пожалуйста, выберите цифру указанных действий...')


def random_keys_generation():

    text = ''
    for i in data_base['shifr']:
        key = 1
        while key == 1:
            repited = 0
            rand1 = random.choice(data_base['abc_and_numbers'])
            rand2 = random.choice(data_base['abc_and_numbers'])
            rand3 = random.choice(data_base['abc_and_numbers'])
            rand4 = random.choice(data_base['abc_and_numbers'])
            rand5 = random.choice(data_base['abc_and_numbers'])
            random_value = rand1 + rand2 + rand3 + rand4 + rand5
            if key == 1:
                data_base['shifr'][i] = random_value
                for l in data_base['shifr']:
                    if l == random_value:
                        repited += 1
                if repited <= 1:
                    text = text + i + "=" + random_value + '\n'
                    data_base['shifr'][i] = random_value
                    key = 0
                    break
    new_keys_file = open('new_keys.txt', 'w+')
    new_keys_file.write(text)
    new_keys_file.close()


def standart_keys():
    data_base['shifr'] = data_base_standart['shifr']


def export_cipher():
    cipher_keys = ''
    for i in data_base['shifr']:
        cipher_keys = cipher_keys + data_base['shifr'][i] + '//'
    print(cipher_keys)
    actually_keys = open('actually_keys.txt', 'w+')
    actually_keys.write(cipher_keys)
    actually_keys.close()


def import_cipher():
    a = -1
    text = input('Введите ключи: ')
    splited_text = text.split('//')
    for i in data_base['shifr']:
        a += 1
        data_base['shifr'][i] = splited_text[a]
    print(splited_text)


cipher_main_menu()