# Generated by Django 2.1.1 on 2018-10-23 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verman', '0003_remove_appdate_user_add'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
