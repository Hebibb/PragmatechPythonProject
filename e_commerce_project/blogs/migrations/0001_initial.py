# Generated by Django 4.0.3 on 2022-04-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('category_tag', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.ImageField(upload_to='blog_pics')),
                ('title', models.CharField(max_length=100)),
                ('explanation', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ('-date',),
            },
        ),
    ]
