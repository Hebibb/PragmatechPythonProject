from django.db import models
# Create your models here.
class Blog(models.Model):
    author=models.CharField(max_length=50)
    category_tag=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='blog_pics')
    title=models.CharField(max_length=100)
    explanation=models.TextField()
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author}\'s  blog'
    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
        ordering=('-date', )