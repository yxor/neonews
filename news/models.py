from django.db import models, IntegrityError
from django.utils.text import slugify
from django.utils.html import strip_tags
from .utils import generate_api_key

import random


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Language(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.code

class Api(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=16, blank=True, editable=False)
    
    
    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

    def save(self, *args, **kwargs):
        self.key = generate_api_key()
        return super(Api, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=500)
    headimage = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, editable=False)
    author = models.CharField(max_length=30, default="random man")
    content = models.TextField()
    show_on_homepage = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def link(self):
        return "/"+self.language.code+"/"+self.category.title+"/"+self.slug+"/"

    def add_ads(self):
        step = 800
        ads_text = '<input type="hidden" name="IL_IN_ARTICLE">'

        if len(self.content) < step:
            self.content += ads_text
            return            

        for i in range( len(self.content)/step ):
            index = i*step + i*len(ads_text)
            self.content = self.content[:index] + ads_text + self.content[index:]

    def snippet(self):
        if len(self.content) < 300:
            return strip_tags(self.content)
        return strip_tags(self.content[:300])+"..."

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:100])
        while True:
            try:
                if self.slug == "" or len(self.slug) < 10:
                    while True:
                        self.slug += str(random.randint(1, 100000))
                        if len(self.slug) >= 20:
                            break
                return super(Article, self).save(*args, **kwargs)
            except IntegrityError:
                self.slug += str(random.randint(1, 10000))

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
