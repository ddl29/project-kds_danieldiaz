from email.policy import default
import os
from pyexpat import model
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()
app = Flask(__name__)
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri = True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=3306
    )

print(mydb)


@app.route('/')
def index():
    return render_template('index.html', title="Gorilla Gang Portfolio", url=os.getenv("URL"))

@app.route('/xuo')
def xuo():
    return render_template('xuo.html', title="Set Lynn Portfolio")

@app.route('/xuo/hobbies')
def xuo_jinja():
    return render_template('xuo_jinja.html', title="Set Hobbies")

@app.route('/chuu')
def chuu():
    return render_template('chuu.html', title="Kaitlyn Chau Portfolio")

@app.route('/chuu/hobbies')
def chuu_hobbies():
    return render_template('chuu_hobbies.html', title="Kaitlyn Chau's Hobbies")

@app.route('/chuu/travel')
def chuu_travel():
    return render_template('chuu_travel.html', title="Kaitlyn Chau's Travel'")

@app.route('/chuu/experience')
def chuu_experience():
    return render_template('chuu_experience.html', title="Kaytlyn's Experience")

@app.route('/chuu/education')
def chuu_education():
    return render_template('chuu_education.html', title="Kaitlyn's Education")

@app.route('/diaz')
def diaz():
    return render_template('diaz.html', title="Daniel Diaz Portfolio")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():   

    #check name
    if "name" not in request.form:
        return "Invalid name", 400
    else:
        name = request.form['name']
        if name == "":
            return "Invalid name", 400

    #check content
    if "content" not in request.form:
        return "Invalid content", 400
    else:
        content = request.form['content']
        if content == "":
            return "Invalid content", 400

    #check email
    if "email" not in request.form:
        return "Invalid email", 400
    else:
        email = request.form['email']
        if email == "" or not re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]+", email):
            return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    name = request.form['name']
    
    matches = {
        'timeline_posts':[
            model_to_dict(p)
            for p in TimelinePost.select().where(TimelinePost.name==name)
        ]
    }
    TimelinePost.delete().where(TimelinePost.name==name).execute()
    return matches

@app.route('/timeline')
def timeline():
    return render_template('timeline.html',title="Timeline")

#Database creation and connection
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
