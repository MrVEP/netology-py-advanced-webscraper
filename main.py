from habr_filters import habr_ru_all_article_filter
from habr_filters import habr_ru_all_preview_filter


def keywords_lister():
    keys = []
    print('Введите ключевое слово для поиска. Оставьте строку пустой, чтобы прекратить добавление ключевых слов:')
    while True:
        key = str(input())
        if not key:
            break
        keys.append(key[0].upper() + key[1:])  # Добавляем ключевые слова с разными регистрами первой буквы
        keys.append(key[0].lower() + key[1:])  # На случай, если с ключевого слова начинается предложение.
    return keys


if __name__ == '__main__':
    keywords = keywords_lister()
    command_list = {'p': habr_ru_all_preview_filter, 'a': habr_ru_all_article_filter}

    if not keywords:
        print('Не было получено ключевых слов.')
    else:
        command = str(input('Введите команду в английском регистре (p - фильтр по превью статьи, a - фильтр по всему '
                            'тексту статьи):'))
        command_list[command](keywords)
