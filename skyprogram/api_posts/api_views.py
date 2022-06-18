import logging

from flask import Blueprint, jsonify, json, abort

from classes.manager import DataManager
from classes.post import Post

api_posts_blueprint = Blueprint('api_posts_blueprint', __name__)

PATH_DATA = "../skyprogram/data/data.json"
PATH_COMMENTS = "../skyprogram/data/comments.json"

data_manager = DataManager(PATH_DATA, PATH_COMMENTS)
api_logger = logging.getLogger("api_logger")


@api_posts_blueprint.route('/')
def greetings_page():
    return "Это API-эндпоинты. Доступные эндпоинты api/posts/ и api/posts/<int:pk>"


@api_posts_blueprint.route('/posts/')
def all_posts():
    """Эндпоинт для всех постов"""
    all_posts: list[Post] = data_manager.load_post_for_api()
    all_posts_as_dict: list[dict] = [post.as_dict() for post in all_posts]
    api_logger.debug("Запрошены все посты")
    return jsonify(all_posts_as_dict), 200


@api_posts_blueprint.route('/posts/<int:pk>')
def posts_by_id(pk: int):
    """Эндпоинт для одного поста"""
    post: Post | None = data_manager.get_post_by_pk(pk)
    if post is None:
        api_logger.debug(f"Запрошен несуществующий пост - {pk}")
        abort(404)

    api_logger.debug(f"Запрошен пост под номером {pk}")
    return jsonify(post), 200


@api_posts_blueprint.errorhandler(404)
def api_error_404(error):
    return f"Ошибка 404"
