# Generated by Django 2.0.5 on 2018-07-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0004_auto_20180717_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=8),
        ),
    ]
