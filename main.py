from pprint import pprint

# Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# 1. Выполните пункты 1-3 задания.

contacts_list_clear = []
temp = []
pattern = r"(\w+)?([ ,])?(\w+)?([ ,])?(\w+)?([ ,])?(\w+)?"
text = str(contacts_list[1])

for i in range(len(contacts_list)):
    phone = re.search(pattern, str(contacts_list[i][0]))
    temp.append([phone.group(1)])
    if phone.group(3) is not None:
        temp[i].append(phone.group(3))
    else:
        temp[i].append((contacts_list[i][1].split(' '))[0])

    for val in temp:
        if val not in contacts_list_clear:
            contacts_list_clear.append(val)

for v in contacts_list_clear:
    for i in contacts_list:

        full_name = [*i[0].split(' '), *i[1].split(' '), i[2]]
        if ((v[0] and v[1]) in full_name) and (full_name[2] not in v) and (full_name[2] != ''):
            v.append(full_name[2])
            v.append(i[3])
            if i[4] != '':
                v.append(i[4])
            else:
                v.append('')

            pattern1 = r"(\+7|8)?\s*[(]?(\d{3})[)]?[\s-]*(\d{3})[\s-]?(\d{2})[\s-]?(\d+)(\s*)[(]?(доб.)?\s*(\d*)[)]?"
            subst_pattern = r"+7 (\2)\3-\4-\5\6\7\8"
            pattern_phone = re.compile(pattern1)
            if len(i[5]) > 0 and i != 0:
                result = pattern_phone.sub(subst_pattern, str(i[5]))
                v.append(result)
            elif i == 0:
                v.append(i[5])
        if (v[0] == full_name[0] and v[1] == full_name[1]) and len(i[4]) > 0:
            v[4] = i[4]

        if (v[0] == full_name[0] and v[1] == full_name[1]) and len(i[6]) > 0:
            v.append(i[6])


for v in contacts_list_clear:
    if len(v) < 7:
        v.append('Электронная почта не указана')
    if v[4] == '':
        v[4] = 'Должность не указана'

pprint(contacts_list_clear)

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:

with open("phonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_clear)
