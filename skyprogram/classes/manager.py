import json
from exceptions import DataSourceBrokenExceptions
from classes.post import Post
from pprint import pprint as pp

#PATH_DATA = "../data/data.json"
#PATH_COMMENTS = "../data/comments.json"


class DataManager:

    def __init__(self, path_data, path_comments):
        self.path_data = path_data
        self.path_comments = path_comments

    def load_data(self):
        """Загружает данные из файла JSON"""
        try:
            with open(self.path_data, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):

            raise DataSourceBrokenExceptions("Файл с данными поврежден")

        return data

    def load_post_for_api(self):
        """Возвращает лист постов для использоания в API-эндпоинтах"""
        post_data = self.load_data()
        list_of_posts = [Post(**post_data) for post_data in post_data]
        return list_of_posts

    def load_comments(self):
        """Загружает комменты из файла JSON"""
        try:
            with open(self.path_comments, 'r', encoding="utf-8") as file:
                comments = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):

            raise DataSourceBrokenExceptions("Файл с данными поврежден")

        return comments

    def get_posts_all(self):
        """возвращает список всех постов"""
        data = self.load_data()
        comments = self.load_comments
        return data, comments

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя.
        Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список, если у пользователя нет постов. """
        posts = self.load_data()
        posts_by_name = []
        for post in posts:
            if user_name.lower() in post["poster_name"].lower():
                posts_by_name.append(post)

        for post in posts:
            if len(posts_by_name) == 0 and user_name.lower() not in post["poster_name"].lower():
                raise ValueError("Такого пользователя нет")

        return posts_by_name

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста.
         Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов."""
        if type(post_id) != int:
            raise TypeError("post_id должен быть int")

        comments = self.load_comments()
        comments_by_id = []
        for comment in comments:
            if post_id == comment["post_id"]:
                comments_by_id.append(comment)

        return comments_by_id

    def search_for_posts(self, query):
        """ Возвращает список постов по ключевому слову"""
        query = str(query).lower()
        posts = self.load_data()
        post_by_query = []
        for post in posts:
            if query in post["content"]:
                post_by_query.append(post)
                continue
        return post_by_query

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору. """
        if type(pk) != int:
            raise TypeError("pk должен быть int")

        posts = self.load_data()
        for post in posts:
            if pk == post["pk"]:
                return post



#dm = DataManager(PATH_DATA, PATH_COMMENTS)
#pp(dm.load_data())
#pp(dm.search_for_posts())
#pp(dm.get_comments_by_post_id(6))
#pp(dm.load_post_for_api())

