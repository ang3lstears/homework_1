import os
# номер 1
'''
def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        print("Ошибка: количество строк должно быть положительным целым числом.")
        return
    if not os.path.isfile(file):
        print(f"Ошибка: файл '{file}' не найден.")
        return
    with open(file, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
    if len(all_lines) < lines:
        lines_to_print = all_lines
    else:
        lines_to_print = all_lines[-lines:]
    for line in lines_to_print:
        print(line.strip())

read_last(3, 'article.txt') '''
# номер 2
'''
def print_docs(directory):
    if not os.path.isdir(directory):
        print(f"Ошибка: Папка '{directory}' не существует или не является директорией.")
        return
    stack = [directory]
    while stack:
        current_directory = stack.pop()
        print("Директория:", current_directory)
        items = os.listdir(current_directory)
        for item in items:
            item_path = os.path.join(current_directory, item)
            if os.path.isdir(item_path):
                stack.append(item_path)
                print(f"  Директория: {item}")
            else:
                print(f"  Файл: {item}")
print_docs('путь_к_папке') '''
#номер 3
'''
def longest_words(file):
    if not os.path.isfile(file):
        print(f"Ошибка: Файл '{file}' не найден.")
        return
    words = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            words.extend(line.strip().split())
    if not words:
        print("Ошибка: Файл пуст.")
        return
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    print("Слова с максимальной длиной:", longest_words)
longest_words('article.txt') '''
# номер 4
import re


def create_text_file():
    filename = input("Введите имя файла (без расширения): ")
    filename = filename.strip() + ".txt"
    with open(filename, 'w', encoding='utf-8') as file:
        print(f"Файл '{filename}' создан. Начинайте вводить текст:")

        while True:
            line = input()
            if not line.strip() or re.match(r'^[^\w\s]+$', line):
                print(f"Файл '{filename}' сохранен.")
                break
            file.write(line + '\n')
create_text_file()