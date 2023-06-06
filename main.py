import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)


def put_in_order():
    '''Функция подготовки ФИО для дальнейшей обработки'''
    contacts = []
    for data in contacts_list:
        split_data = ' '.join(data[:3]).split(' ')
        contacts.append([split_data[0], split_data[1], split_data[2], data[3], data[4], data[5], data[6]])
    return contacts
put_in_order()

def phone_numbers():
    '''Функция поиска и приведения к единому стандарту тф номеров'''
    contacts = put_in_order()
    pattern = r'(\+7|8|7)?\s*\(?(\d{3})\)?\s*[-]?(\d{2,5})[-]?(\d{2})[-]?(\d{2})\s*\(?(доб\.?)?\s*(\d{2,5})?\)?'
    new_phone_num = r'+7(\2)\3-\4-\5 \6\7'
    for number in contacts:
        res = re.sub(pattern, new_phone_num, number[5])
        number[5] = res
    return contacts
phone_numbers()

def list_for_load():
    '''Функция очистки списка от повторяющихся значений'''
    contacts = phone_numbers()
    for info in contacts:
        last_name = info[0]
        name = info[1]
        for new_info in contacts:
            new_last_name = new_info[0]
            new_name = new_info[1]
            if last_name == new_last_name and name == new_name:
                if info[2] == '':
                    info[2] = new_info[2]
                if info[3] == '':
                    info[3] = new_info[3]
                if info[4] == '':
                    info[4] = new_info[4]
                if info[5] == '':
                    info[5] = new_info[5]
                if info[6] == '':
                    info[6] = new_info[6]
    ready_contact_list = []
    for data in contacts:
        if data not in ready_contact_list:
            ready_contact_list.append(data)
    return ready_contact_list


if __name__ == '__main__':
    put_in_order()
    phone_numbers()
    pprint(list_for_load())


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_for_load())
