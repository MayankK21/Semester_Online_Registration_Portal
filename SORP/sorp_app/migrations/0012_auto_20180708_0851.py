# Generated by Django 2.0.6 on 2018-07-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0011_auto_20180706_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]