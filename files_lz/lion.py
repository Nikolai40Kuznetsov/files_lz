import re
import csv
import string
import matplotlib.pyplot as plt
# создаём словари
frequency = {}
number = {}   
# открываем файл  
with open('lion.txt', 'r', encoding='utf-8') as document_text:
    text_string = document_text.read().lower()
words_count = len(text_string.split())
# считаем слова
match_pattern_1 = re.findall(r'\b[a-z]{2,25}\b', text_string)
match_pattern_2 = re.findall(r'\b[а-я]{2,25}\b', text_string)
for word in match_pattern_1 + match_pattern_2:
    frequency[word] = frequency.get(word, 0) + 1
# считаем буквы
english_letters = re.findall(r'[a-z]', text_string)
russian_letters = re.findall(r'[а-я]', text_string)
for letter in english_letters + russian_letters:
    number[letter] = number.get(letter, 0) + 1
with open("lion.csv", mode="w", encoding='utf-8', newline='') as w_file:
    # заполяем таблицу
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(["Слово", "Частота встречи, раз", "Частота встречаемости в %"])
    for word in frequency:
        percentage = (frequency[word] / words_count) * 100
        file_writer.writerow([word, frequency[word], percentage])
for letter in number:
    print(letter, number[letter])
# строим график
plt.figure(figsize=(12, 6))
sorted_russian_letters = sorted([letter for letter in number if re.match(r'[а-я]', letter)], key=lambda x: x)
sorted_counts = [number[letter] for letter in sorted_russian_letters]
plt.bar(sorted_russian_letters, sorted_counts, color='blue')
plt.xlabel('Буквы')
plt.ylabel('Количество')
plt.title('Количество русских букв в тексте')
plt.grid(axis='y')
plt.tight_layout()
plt.show()