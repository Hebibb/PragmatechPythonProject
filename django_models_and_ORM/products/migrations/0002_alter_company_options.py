# Generated by Django 4.0.3 on 2022-03-29 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('-cr_date',), 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]
