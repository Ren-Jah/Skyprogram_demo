from flask import Blueprint, render_template, request, current_app

from classes.manager import DataManager


main_blueprint = Blueprint('main_blueprint', __name__)

PATH_DATA = "../skyprogram/data/data.json"
PATH_COMMENTS = "../skyprogram/data/comments.json"

data_manager = DataManager(PATH_DATA, PATH_COMMENTS)


@main_blueprint.route('/')
def main():
    posts, comments = data_manager.get_posts_all()
    return render_template('index.html', posts=posts, comments=comments)


@main_blueprint.route('/search', methods=["GET", "POST"])
def page_post_form():
    query = request.args['s']

    search_for_posts = data_manager.search_for_posts(query)
    nums_searched_posts = len(search_for_posts)

    return render_template('search.html', query=query,
                           search_for_posts=search_for_posts,
                           nums_searched_posts=nums_searched_posts)
