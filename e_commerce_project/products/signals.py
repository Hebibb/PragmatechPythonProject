from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from products.models import Product
User=get_user_model()

def slug_save(instance,created, *args, **kwargs):
    if created:
        Product.objects.filter(id=instance.id).update(slug=slugify(instance.name))
    
post_save.connect(slug_save,sender=Product)