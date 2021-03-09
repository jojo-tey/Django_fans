from django.contrib import admin
from post.models import Post, PostFileContent

# Register your models here.
admin.site.register(Post)
admin.site.register(PostFileContent)
