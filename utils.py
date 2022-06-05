import json
from exteptions import *


def load_posts(path):
    """Загружает JSON файл"""
    try:
        with open(path, "r", encoding="UTF-8") as file:
            posts = json.load(file)
        return posts
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError("Не удалось декодировать данные JSON, или такого файла не существует")


def search_posts(search, path):
    """Ищет посты по вхождению букв"""
    posts = load_posts(path)
    filtered_posts = []

    for post in posts:
        if search in post['content']:
            filtered_posts.append(post)

    return filtered_posts


def save_posts(posts, path):
    """ Сохраняет посты """
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(posts, file)

