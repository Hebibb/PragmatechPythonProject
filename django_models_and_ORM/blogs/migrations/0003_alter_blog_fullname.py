# Generated by Django 4.0.3 on 2022-03-28 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_author_alter_blog_content_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fullname',
            field=models.ForeignKey(default='Unknown', null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.author'),
        ),
    ]
