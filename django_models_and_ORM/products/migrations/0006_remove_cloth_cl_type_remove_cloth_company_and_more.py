# Generated by Django 4.0.3 on 2022-03-30 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cl_company_cl_type_cloth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='cl_type',
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='company',
        ),
        migrations.DeleteModel(
            name='Cl_company',
        ),
        migrations.DeleteModel(
            name='Cl_type',
        ),
        migrations.DeleteModel(
            name='Cloth',
        ),
    ]
