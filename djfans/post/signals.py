from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import Post, Stream


@receiver(post_save, sender=Post)
def new_post_save(sender, **kwargs):
    post = kwargs['instance'].post
    post.save()
