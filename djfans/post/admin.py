from django.contrib import admin
from post.models import Post, PostFileContent, Stream, Likes

# Register your models here.
admin.site.register(Post)
admin.site.register(Stream)
admin.site.register(PostFileContent)
admin.site.register(Likes)
