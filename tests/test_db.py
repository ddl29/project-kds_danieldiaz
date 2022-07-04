import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()
    
    def test_timeline_post(self):
        # creating 2 timeline posts
        first_post = TimelinePost.create(name = 'John Doe', email = 'john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name = 'Jane Doe', email = 'jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        # getting timeline posts and asserting that they are correct
        posts = {
            'timeline_posts':[
                model_to_dict(p)
                for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
            ]
        }

        assert posts['timeline_posts'][0]['id'] == 2
        assert posts['timeline_posts'][0]['name'] == 'Jane Doe'
        assert posts['timeline_posts'][0]['email'] == 'jane@example.com'
        assert posts['timeline_posts'][0]['content'] == 'Hello world, I\'m Jane!'

        assert posts['timeline_posts'][1]['id'] == 1
        assert posts['timeline_posts'][1]['name'] == 'John Doe'
        assert posts['timeline_posts'][1]['email'] == 'john@example.com'
        assert posts['timeline_posts'][1]['content'] == 'Hello world, I\'m John!'
        
