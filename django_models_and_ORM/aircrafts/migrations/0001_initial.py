# Generated by Django 4.0.3 on 2022-04-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airliner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, default='Unknown', null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fligth_status', models.CharField(blank=True, choices=[('Onair', 'onair'), ('Onland', 'onland')], default='UNKNOWN', max_length=40, null=True)),
                ('plane_name', models.CharField(blank=True, max_length=40, null=True)),
                ('about', models.TextField(blank=True, max_length=300, null=True)),
                ('fl_score', models.IntegerField(default=0)),
                ('model_year', models.DateTimeField(auto_now_add=True)),
                ('rent_price', models.IntegerField(default=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='planePics/')),
                ('airliner', models.ManyToManyField(to='aircrafts.airliner')),
            ],
        ),
    ]
