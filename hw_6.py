import re

while True:
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    start = int(input('Выберите пункт: \n'
                      '1 - подсчет имен и фамилии: \n'
                      '2 - подсчет email: \n'
                      '3 - подсчет название файлов: \n'
                      '4 - подсчет цветов: \n'
                      '5 - завершение программы\n'))
    if start == 1:
            name_surname = re.findall(r'\b[A-Z][A-Za-z\-]+\s[A-Za-z\'\.\- ]+\b', content)
            with open('name_surname.txt', 'w', encoding='UTF-8') as file:
                for i in name_surname:
                    file.write(f'{i}\n')

    elif start == 2:
            name_email = re.findall(r'(\b([\w\-]+)(@)[\w\-]+(\.[\w]+))+', content)
            with open('name_email.txt', 'w', encoding='UTF-8') as file:
                for i in name_email:
                    file.write(f'{i[0]}\n')

    elif start == 3:
            name_file = re.findall(r'\t[a-zA-Z]+\.[a-z\d]+', content)
            with open('name_file.txt', 'w', encoding='UTF-8') as file:
                for i in name_file:
                    file.write(f'{i[1:]}\n')

    elif start == 4:
            name_color = re.findall(r'#[0-9A-Fa-f]+', content)
            with open('name_color.txt', 'w', encoding='UTF-8') as file:
                for i in name_color:
                    file.write(f'{i}\n')

    elif start == 5:
        print('Вы завершили программу.')
        break