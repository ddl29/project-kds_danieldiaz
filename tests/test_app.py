import unittest
import os
os.environ['TESTING'] = 'true'

# import flask app
from app import app
from app import TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Gorilla Gang Portfolio</title>" in html
        # more tests relating to the home page
        assert "<h1>Kaitlyn Chau</h1>" in html
        assert "<h1>Set Lynn</h1>" in html
        assert "<h1>Dani Diaz</h1>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json['timeline_posts']) == 0
        # more tests relating to the /api/timeline_post GET and POST apis
        first_post = {'name': 'John Doe', 'email': 'john@example.com', 'content':'Hello world, I\'m John!'}

        # testing post
        response = self.client.post('/api/timeline_post', data= first_post)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json['id'] == 1
        assert json['name'] == 'John Doe'
        assert json['email'] == 'john@example.com'
        assert json['content'] == 'Hello world, I\'m John!'

        # Running get to see if the post was successful
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json['timeline_posts']) == 1
        assert json['timeline_posts'][0]['id'] == 1
        assert json['timeline_posts'][0]['name'] == 'John Doe'
        assert json['timeline_posts'][0]['email'] == 'john@example.com'
        assert json['timeline_posts'][0]['content'] == 'Hello world, I\'m John!'

        # adding another post
        second_post = {'name': 'Jane Doe', 'email': 'jane@example.com', 'content':'Hello world, I\'m Jane!'}

        response = self.client.post('/api/timeline_post', data= second_post)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json['id'] == 2
        assert json['name'] == 'Jane Doe'
        assert json['email'] == 'jane@example.com'
        assert json['content'] == 'Hello world, I\'m Jane!'

        # Running get to see if the post was successful
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json['timeline_posts']) == 2
        assert json['timeline_posts'][0]['id'] == 2
        assert json['timeline_posts'][0]['name'] == 'Jane Doe'
        assert json['timeline_posts'][0]['email'] == 'jane@example.com'
        assert json['timeline_posts'][0]['content'] == 'Hello world, I\'m Jane!'

        # more tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html # check that the title is correct
        assert "<h1>All posts</h1>" in html # check that the header is present
        assert "<body onload=\"httpGetAsync('api/timeline_post')\">" in html # check that the get request is called
        assert "<form id=\"form\">" in html # check that a form exists
        assert "fetch('/api/timeline_post', {method: 'POST',body: payload,})" # check that post request is called

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data = {
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid name" in response_text

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid content" in response_text

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid email" in response_text