# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_file():
    # Чтение данных из строки
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def get_sort(data):
    # Сортировка по возрасту по возрастанию
    _new_data = sorted(data, key=lambda d: d['age'])
    return _new_data


def get_filter(_new_data):
    # Фильтрация
    result_data = [person for person in _new_data if person['age'] > 10]
    return result_data


def main():
    data = get_file()
    get_sort(data)
    _new_data = get_sort(data)
    print(get_filter(_new_data))


if __name__ == '__main__':
    main()
