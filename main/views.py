from flask import Blueprint, render_template, request
from utils import search_posts
from config import POST_PATH
import logging


catalog_blueprint = Blueprint('catalog_blueprint', __name__)

logging.basicConfig(filename="logger.log")


@catalog_blueprint.route("/")
def page_index():
    """ Главная страница """
    s = request.args.get('s')
    return render_template("index.html")


@catalog_blueprint.route("/search", methods=["GET"])
def page_search():
    """ Вьюшка для поиска постов """
    s = request.args['s']
    logging.info("Выполняется поиск")
    posts = search_posts(s, POST_PATH)

    return render_template("post_list.html", s=s, posts=posts)
