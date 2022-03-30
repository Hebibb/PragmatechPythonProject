# Generated by Django 4.0.3 on 2022-03-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_song_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cl_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=150)),
                ('city', models.CharField(default='Unknown', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cl_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField(default='Nothing')),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genders', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True, max_length=80, null=True)),
                ('size', models.CharField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('Xlarge', 'XL'), ('XXLarge', 'XXL'), ('XXXLarger', 'XXXL')], max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('cl_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cl_type')),
                ('company', models.ManyToManyField(to='products.cl_company')),
            ],
        ),
    ]