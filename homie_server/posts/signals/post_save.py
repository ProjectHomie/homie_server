from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, create, **kwargs):
    from hashids import Hashids

    if not instance.hash_id:
        hashids = Hashids(salt="homei_server", min_length=6)

        instance.hasj_id = hashids.encode(instance.id)
        instance.save()
