import os
print("number 1")
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

read_last(3, 'article.txt')
print("number 2")
def print_docs(directory):
    if not os.path.exists(directory):
        print(f"Путь {directory} не существует.")
        return
    for root, dirs, files in os.walk(directory):
        print(f'Directory: {root}')
        for dir_name in dirs:
            print(f'  Subdirectory: {os.path.join(root, dir_name)}')
        for file_name in files:
            print(f'  File: {os.path.join(root, file_name)}')
print_docs('/Users/atsai/PycharmProjects/PythonProject')
print("number 3")
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
longest_words('article.txt')
print("number 4")
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
