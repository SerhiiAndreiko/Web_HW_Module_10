import django
import os
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10_project.settings")

django.setup()

client = MongoClient("mongodb://localhost")
db = client.hw

authors = db.authors.find()

for author in authors:
    print(author)