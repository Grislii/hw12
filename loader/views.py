from flask import Blueprint, render_template, request, send_from_directory
from config import UPLOAD_FOLDER, POST_PATH
from utils import load_posts, save_posts
from exteptions import *

import logging

logging.basicConfig(filename="logger.log")

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route("/form")
def page_form_post():
    """ В этой вьюшке идет сбор информации о новом посте """

    return render_template("post_form.html")


@loader_blueprint.route("/uploaded", methods=["POST"])
def page_add_post():
    """ В этой вьюшке добавляется пост """
    posts = load_posts(POST_PATH)

    allowed_extension = ["jpg", "jpeg", "png"]

    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        logging.info("Остуствует часть данных при загрузки нового поста")
        return "Остуствует картинка или текст"

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    if picture_path.split(".")[-1] in allowed_extension:
        picture.save(picture_path)
    else:
        logging.info("Был загружен неверный формат изображения")
        raise FormatPictureError("Был загружен неверный формат изображения")

    new_post = {"pic": picture_path, "content": content}

    posts.append(new_post)

    save_posts(posts, POST_PATH)

    return render_template("post_uploaded.html", newpost=new_post)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    """ Отдача доступа пользователю к папке uploads """
    return send_from_directory("uploads", path)
