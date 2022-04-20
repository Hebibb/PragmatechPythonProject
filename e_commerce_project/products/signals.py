from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from products.models import Product
from django.dispatch import receiver
User=get_user_model()
@receiver(post_save,sender=Product)
def slug_save(instance,created, *args, **kwargs):
    if created:
        Product.objects.filter(id=instance.id).update(slug=slugify(instance.name))
    
# post_save.connect(slug_save,sender=Product)

#other vesion
#this version been cut from modules.py
# def slug_save(instance,*args,**kwargs):
#         Product.objects.filter(id=instance.id).update(slug=slugify(instance.name))

# post_save.connect(slug_save,sender=Product)