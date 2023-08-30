'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть
10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''
import re
from collections import Counter
import requests
from bs4 import BeautifulSoup


def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()


def get_most_common_words(text, num_words=10):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    word_counts = Counter(words)
    return word_counts.most_common(num_words)


# Пример URL (замените на нужный вам)
sample_url = "https://ru.wikipedia.org/wiki/GeekBrains"

# Получение текста со страницы по указанной ссылке
sample_text = get_text_from_url(sample_url)

# Получение 10 наиболее часто встречающихся слов
most_common_words = get_most_common_words(sample_text, num_words=10)

# Вывод результатов
print('10 самых часто встречаемых слов: ')
for i, (word, count) in enumerate(most_common_words, start=1):
    print(f"{i}. {word}: {count}")
