import random


data_base_standart = {
    'shifr': {
        'а': 'frt0',  #
        'б': 'hyu6',  #
        'в': 'k7iy',
        'г': 's4hf',
        'д': 'lp8i',
        'е': 'nh9o',  #
        'ё': '0loh',
        'ж': 'g4fv',  #
        'з': 'n7hj',
        'и': 'ky8h',
        'й': 'm5g7',
        'к': 'lgt4',
        'л': 'fs3p',
        'м': 'nn9f',
        'н': 'xt28',
        'о': 'l5d3',
        'п': 'jgg6',
        'р': 'pwhl',
        'с': 'hm2x',
        'т': 'mmtj',
        'у': 'psxk',
        'ф': 'lsmx',
        'х': 'umwx',
        'ц': 'ge6y',
        'ч': 'kp0o',
        'ш': 'ntlk',
        'щ': 'ku7g',
        'ъ': 'mp3f',
        'ы': 'lui8',
        'ь': 'hn5p',
        'э': 'sst5',
        'ю': 'tst5',
        'я': 'tnt6',
        '.': 'mi4p',
        ',': 'vpy7',
        ';': 'orn7',
        ':': 'jj7k',
        '"': 'lxw6',
        '\'': 'm0oi',
        '(': 'v0po',
        ')': 'v5f0',
        '`': 'kt4r',
        '!': 'jlo0',
        '?': '5gy6',
        '1': 'j7g6',
        '2': 'll0n',
        '3': 'ge4r',
        '4': 'mk6t',
        '5': 'vx0r',
        '6': 'jof3',
        '7': 'n7d3',
        '8': 'l0l0',
        '9': 'jt5o',
        '0': 'nv0p',
        # Заглавные
        'А': 'cfrt0',
        'Б': 'chyu6',
        'В': 'ck7iy',
        'Г': 'cs4hf',
        'Д': 'clp8i',
        'Е': 'cnh9o',
        'Ё': 'c0loh',
        'Ж': 'cg4fv',
        'З': 'cn7hj',
        'И': 'cky8h',
        'Й': 'cm5g7',
        'К': 'clgt4',
        'Л': 'cfs3p',
        'М': 'cnn9f',
        'Н': 'cxt28',
        'О': 'cl5d3',
        'П': 'cjgg6',
        'Р': 'cpwhl',
        'С': 'chm2x',
        'Т': 'cmmtj',
        'У': 'cpsxk',
        'Ф': 'clsmx',
        'Х': 'cumwx',
        'Ц': 'cge6y',
        'Ч': 'ckp0o',
        'Ш': 'cntlk',
        'Щ': 'cku7g',
        'Ъ': 'cmp3f',
        'Ы': 'clui8',
        'Ь': 'chn5p',
        'Э': 'csst5',
        'Ю': 'ctst5',
        'Я': 'ctnt6',
        ' ': 'bpx3',
        'A': 'chgu7',
        'B': 'cvh8u',
        'C': 'ckpw3',
        'D': 'cg7j8',
        'E': 'cl2o0',
        'F': 'cp00p',
        'G': 'cju7t',
        'H': 'cy2lp',
        'I': 'cy5p0',
        'J': 'cpl5t',
        'K': 'cni2e',
        'L': 'cj9p7',
        'M': 'ch2pl',
        'N': 'cb6q2',
        'O': 'cpgu7',
        'P': 'ch4c9',
        'Q': 'cjm4e',
        'R': 'cppp0',
        'S': 'chlhj',
        'T': 'cwp02',
        'U': 'cnnxp',
        'V': 'c7ko9',
        'W': 'cwpn1',
        'X': 'crkrm',
        'Y': 'cs2l2',
        'Z': 'cp87y',
        'a': 'hgu7',
        'b': 'vh8u',
        'c': 'kpw3',
        'd': 'g7j8',
        'e': 'l2o0',
        'f': 'p00p',
        'g': 'ju7t',
        'h': 'y2lp',
        'i': 'y5p0',
        'j': 'pl5t',
        'k': 'ni2e',
        'l': 'j9p7',
        'm': 'h2pl',
        'n': 'b6q2',
        'o': 'pgu7',
        'p': 'h4c9',
        'q': 'jm4e',
        'r': 'ppp0',
        's': 'hlhj',
        't': 'wp02',
        'u': 'nnxp',
        'v': '7ko9',
        'w': 'wpn1',
        'x': 'rkrm',
        'y': 's2l2',
        'z': 'p87y',
        '@': 'l1l2',
        '#': 'mm6i',
        '%': 'npo5',
        '&': 'vpsp',
        '^': 'nnnr',
},
    'abc_and_numbers': ['0','1','2','3','4', '5', '6', '7', '8', '9', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],

}


data_base = {
    'shifr': {
        'а': 'frt0',  #
        'б': 'hyu6',  #
        'в': 'k7iy',
        'г': 's4hf',
        'д': 'lp8i',
        'е': 'nh9o',  #
        'ё': '0loh',
        'ж': 'g4fv',  #
        'з': 'n7hj',
        'и': 'ky8h',
        'й': 'm5g7',
        'к': 'lgt4',
        'л': 'fs3p',
        'м': 'nn9f',
        'н': 'xt28',
        'о': 'l5d3',
        'п': 'jgg6',
        'р': 'pwhl',
        'с': 'hm2x',
        'т': 'mmtj',
        'у': 'psxk',
        'ф': 'lsmx',
        'х': 'umwx',
        'ц': 'ge6y',
        'ч': 'kp0o',
        'ш': 'ntlk',
        'щ': 'ku7g',
        'ъ': 'mp3f',
        'ы': 'lui8',
        'ь': 'hn5p',
        'э': 'sst5',
        'ю': 'tst5',
        'я': 'tnt6',
        '.': 'mi4p',
        ',': 'vpy7',
        ';': 'orn7',
        ':': 'jj7k',
        '"': 'lxw6',
        '\'': 'm0oi',
        '(': 'v0po',
        ')': 'v5f0',
        '`': 'kt4r',
        '!': 'jlo0',
        '?': '5gy6',
        '1': 'j7g6',
        '2': 'll0n',
        '3': 'ge4r',
        '4': 'mk6t',
        '5': 'vx0r',
        '6': 'jof3',
        '7': 'n7d3',
        '8': 'l0l0',
        '9': 'jt5o',
        '0': 'nv0p',
        # Заглавные
        'А': 'cfrt0',
        'Б': 'chyu6',
        'В': 'ck7iy',
        'Г': 'cs4hf',
        'Д': 'clp8i',
        'Е': 'cnh9o',
        'Ё': 'c0loh',
        'Ж': 'cg4fv',
        'З': 'cn7hj',
        'И': 'cky8h',
        'Й': 'cm5g7',
        'К': 'clgt4',
        'Л': 'cfs3p',
        'М': 'cnn9f',
        'Н': 'cxt28',
        'О': 'cl5d3',
        'П': 'cjgg6',
        'Р': 'cpwhl',
        'С': 'chm2x',
        'Т': 'cmmtj',
        'У': 'cpsxk',
        'Ф': 'clsmx',
        'Х': 'cumwx',
        'Ц': 'cge6y',
        'Ч': 'ckp0o',
        'Ш': 'cntlk',
        'Щ': 'cku7g',
        'Ъ': 'cmp3f',
        'Ы': 'clui8',
        'Ь': 'chn5p',
        'Э': 'csst5',
        'Ю': 'ctst5',
        'Я': 'ctnt6',
        ' ': 'bpx3',
        'A': 'chgu7',
        'B': 'cvh8u',
        'C': 'ckpw3',
        'D': 'cg7j8',
        'E': 'cl2o0',
        'F': 'cp00p',
        'G': 'cju7t',
        'H': 'cy2lp',
        'I': 'cy5p0',
        'J': 'cpl5t',
        'K': 'cni2e',
        'L': 'cj9p7',
        'M': 'ch2pl',
        'N': 'cb6q2',
        'O': 'cpgu7',
        'P': 'ch4c9',
        'Q': 'cjm4e',
        'R': 'cppp0',
        'S': 'chlhj',
        'T': 'cwp02',
        'U': 'cnnxp',
        'V': 'c7ko9',
        'W': 'cwpn1',
        'X': 'crkrm',
        'Y': 'cs2l2',
        'Z': 'cp87y',
        'a': 'hgu7',
        'b': 'vh8u',
        'c': 'kpw3',
        'd': 'g7j8',
        'e': 'l2o0',
        'f': 'p00p',
        'g': 'ju7t',
        'h': 'y2lp',
        'i': 'y5p0',
        'j': 'pl5t',
        'k': 'ni2e',
        'l': 'j9p7',
        'm': 'h2pl',
        'n': 'b6q2',
        'o': 'pgu7',
        'p': 'h4c9',
        'q': 'jm4e',
        'r': 'ppp0',
        's': 'hlhj',
        't': 'wp02',
        'u': 'nnxp',
        'v': '7ko9',
        'w': 'wpn1',
        'x': 'rkrm',
        'y': 's2l2',
        'z': 'p87y',
        '@': 'l1l2',
        '#': 'mm6i',
        '%': 'npo5',
        '&': 'vpsp',
        '^': 'nnnr',
},
    'abc_and_numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],

}
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
    cipher_file = open('cipher_text.txt', 'w+')
    cipher_file.write(' ')
    cipher_file.close()

def main_menu():
    while True:
        print(' ')
        print('*** Меню ***')
        print('1. Шифрация')
        print('2. Дешифрация')
        print('3. Очистка кэша')
        print('4. Генерация новых ключей')
        print('5. Сброс до стандартных ключей')
        print('6. Экспот ключей')
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
            print(data_base['shifr'])
        elif choise == '6':
            export_cipher()
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


# def import_cipher():
#     cipher_keys = input('Введите код ключей: ')
#     splited_keys = cipher_keys.split('//')
#     for i in data_base['shifr']:
#         data_base['shifr'][i] = splited_keys     # Доделать вставку значения в ключи по индексу списка splited_keys
#

main_menu()