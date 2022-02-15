import requests
from bs4 import BeautifulSoup


def habr_ru_all_preview_filter(keys: list):
    headers = {
        'Accept': '*/*',
        "User-Agent": 'Chrome/98.0.4758.82'
    }
    response = requests.get('https://habr.com/ru/all/', headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('article')
    found_articles = False
    for article in articles:
        for key in keys:
            time = article.find('time').get('title')
            header = article.find('h2').text
            link = 'habr.com' + article.find('h2').find('a').get('href')
            preview = article.find('p')
            if preview is None:
                preview = article.find(class_="article-formatted-body article-formatted-body_version-1").get_text()
            else:
                preview = preview.text

            if key in header or key in preview:
                print(f'{time} - {header} - {link}')
                found_articles = True
                break
    if not found_articles:
        print('По Вашим ключевым словам ничего не найдено.')


def habr_ru_all_article_filter(keys: list):
    headers = {
        'Accept': '*/*',
        "User-Agent": 'Chrome/98.0.4758.82'
    }
    response = requests.get('https://habr.com/ru/all/', headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('article')
    found_articles = False
    for article in articles:
        for key in keys:
            time = article.find('time').get('title')
            header = article.find('h2').text
            link = 'habr.com' + article.find('h2').find('a').get('href')
            headers = {
                'Accept': '*/*',
                "User-Agent": 'Chrome/98.0.4758.82'
            }
            article_page = requests.get('http://' + link, headers=headers)
            article_page.raise_for_status()

            soup_2 = BeautifulSoup(article_page.text, features='html.parser')
            article_text = soup_2.find(id="post-content-body").get_text()

            if key in header or key in article_text:
                print(f'{time} - {header} - {link}')
                found_articles = True
                break
    if not found_articles:
        print('По Вашим ключевым словам ничего не найдено.')
