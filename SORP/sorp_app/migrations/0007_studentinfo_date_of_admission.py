# Generated by Django 2.0.6 on 2018-07-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0006_remove_studentinfo_date_of_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='date_of_admission',
            field=models.DateField(auto_now=True),
        ),
    ]
