from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    
    
    def ready(self):
        import cmdbox.products.signals 
    # def ready(self):
    #     import 
