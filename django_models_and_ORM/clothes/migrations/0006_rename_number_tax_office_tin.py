# Generated by Django 4.0.3 on 2022-04-01 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_alter_cl_company_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tax_office',
            old_name='number',
            new_name='TIN',
        ),
    ]