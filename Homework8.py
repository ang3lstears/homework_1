import re
print("numbeer 1")
def replace(text):
    pattern = r'\b([01]?[0-9]|2[0-3]):([0-5]?[0-9])(:([0-5]?[0-9]))?\b'
    res = re.sub(pattern, "(TBD)", text)
    return res
s = input('Введите строку: ')
tbd = replace(s)
print(tbd)
print("number 2")
def find_abr(text):
    pattern = r'[А-Я]{2,}'
    abr = re.findall(pattern, text)
    abr_str = ' '.join(abr)

    return abr_str
s = input('Введите строку: ')

vse_abr = find_abr(s)
print(vse_abr)