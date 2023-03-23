from bs4 import BeautifulSoup
import requests
import wikipedia
import json
import logging
import argparse
import os


URL_WIKI = "https://en.wikipedia.org"
os.environ["WIKI_FILE"] = "wiki.json"
os.environ.setdefault('DEBUG', 'True')


def generate_soup(url):
    # выполняем базовую настройку системы ведения журнала
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("log")  # задаем свое имя регистратора Logger
    page = requests.get(url)  # получить URL
    soup = BeautifulSoup(page.content, "html.parser")  # очистить веб-страницу
    logger.info(soup.title.string)  # выводим инфо
    return soup


def parser_wikipedia(name_page, link, depth, set_elem, json_file):
    max_links = [1000]
    depth -= 1
    if depth >= 0 and max_links[0] >= 0:
        try:
            soup = generate_soup(link)
            all_links = soup.find(id="bodyContent").find_all(
                "a", href=True)  # Получаем все ссылки/теги
            source_name = name_page
            for value in all_links:
                name_page = value.get("title")
                link = value.get("href")
                # Нас интересуют только другие статьи вики
                if value["href"].find("/wiki/", 0, 6) == -1:
                    continue
                if name_page is None:
                    continue
                if name_page not in set_elem:
                    # Добавляем заданный элемент в набор
                    set_elem.add(name_page)
                    json_file["nodes"].append(  # Добавляем в список узлы
                        {"name_page": name_page, "link_page": URL_WIKI + link})
                    json_file["edges"].append(  # Добавляем в список ребра
                        {"from": source_name, "to": name_page})
                    parser_wikipedia(name_page, URL_WIKI + link,
                                     depth, set_elem, json_file)
                    max_links[0] -= 1
        except BaseException:
            print("Error")


def parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=str, help="starting page",
                        required=False, default="Erdős number")
    parser.add_argument("-d", type=int, help="depth",
                        required=False, default=3)
    args = parser.parse_args()
    return args


def get_wikipedia(link):
    try:
        return wikipedia.page(link, auto_suggest=False).url
    except wikipedia.PageError as p:
        print(p)
        exit(0)
    except wikipedia.DisambiguationError as d:
        link = d.options[0]
        return wikipedia.page(link, auto_suggest=False)


def generate_json():
    return {"nodes": list(), "edges": list()}


def write_to_json(data):
    with open("wiki.json", "w", encoding="UTF-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    print("Let's gooo...")
    arguments = parser_args()
    url = get_wikipedia(str(arguments.p))
    json_file = generate_json()
    set_elem = set()
    parser_wikipedia(arguments.p, url, arguments.d, set_elem, json_file)
    write_to_json(json_file)
    print("Wiki parsed, the program is completed. View the wiki.json!")

    """
        Для запуска скрипта:
        python3 cache_wiki.py -p 'Erdős number'
        python3 cache_wiki.py -d 3
        Либо без аргументов:
        python3 cache_wiki.py
    """
