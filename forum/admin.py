from django.contrib import admin
from .models import Category, Topic, Forum, Post

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Forum)
admin.site.register(Post)
