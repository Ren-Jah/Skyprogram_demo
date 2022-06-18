from flask import Blueprint, render_template, request, current_app

from classes.manager import DataManager


one_post_blueprint = Blueprint('one_post_blueprint', __name__)

PATH_DATA = "../skyprogram/data/data.json"
PATH_COMMENTS = "../skyprogram/data/comments.json"

data_manager = DataManager(PATH_DATA, PATH_COMMENTS)


@one_post_blueprint.route('/posts/<int:pk>/')
def user_post(pk):
    post = data_manager.get_post_by_pk(pk)
    comments = data_manager.get_comments_by_post_id(pk)
    number_of_comments = len(comments)
    return render_template('post.html', post=post,
                           comments=comments,
                           number_of_comments=number_of_comments)
