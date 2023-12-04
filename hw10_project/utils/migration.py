import os

import django
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")

django.setup()
from quotes.models import Quotes, Tags, Authors

client = MongoClient("mongodb://localhost")
db = client.hw

authors = db.authors.find()

for author in authors:
    Authors.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )
quotes = db.quotes.find()
for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tags.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quotes.objects.filter(quote=quote['quote'])))
    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Authors.objects.get(fullname=author['fullname'])
        q = Quotes.objects.create(quote=quote['quote'], author=a)
        for tag in tags:
           q.tags.add(tag)
