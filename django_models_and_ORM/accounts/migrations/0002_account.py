# Generated by Django 4.0.3 on 2022-04-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='your name', max_length=50)),
                ('lastname', models.CharField(help_text='your surname', max_length=50)),
                ('email', models.EmailField(default='_@_', max_length=254)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('image', models.ImageField(upload_to='accounts/')),
            ],
        ),
    ]
