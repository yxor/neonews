from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Article, Category, Language, Api


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Api)
admin.site.unregister(User)
admin.site.unregister(Group)
