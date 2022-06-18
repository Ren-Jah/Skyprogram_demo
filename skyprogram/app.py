from flask import Flask, render_template
import logging
from main.views import main_blueprint
from one_post.views import one_post_blueprint
from user_feed.views import user_feed_blueprint
from api_posts.api_views import api_posts_blueprint
from api_logs import loggers

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(one_post_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(api_posts_blueprint, url_prefix="/api")

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

loggers.create_api_logger()

logger = logging.getLogger('api.log')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('server_error.html')


if __name__ == '__main__':
    app.run(debug=True)
