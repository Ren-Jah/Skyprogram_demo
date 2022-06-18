import pytest

from app import app

path_data = "data/data.json"
path_comments = "data/comments.json"


class testApi:

    @pytest.fixture
    def app_instance(self):
        return app

    def test_foo(self):
        assert 1 == 1

