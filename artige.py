import json

from celery import Celery
import urllib.request
import os

# Where the downloaded files will be stored
from WebUI.models import Post
from django.conf import settings  # noqa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
BASEDIR="/home/rome/Projects/artigeUI"

# Create the app and set the broker location (RabbitMQ)
app = Celery('artige',
             broker='pyamqp://guest@localhost//')

@app.task
def insert_post(json_obj):
    """
    Download a page and save it to the BASEDIR directory
      url: the url to download
      filename: the filename used to save the url in BASEDIR
    """
    test = json.dump(json_obj)
    title = test['title']
    images = test['images']
    tags = test['tags']
    description = test['description']
    temp = Post()
    temp.title = title
    temp.images = images
    temp.tags = tags
    temp.description = description
    temp.save()
    print(test)