# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from news_django.models import News_model

class NewsScrapyItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = News_model
    