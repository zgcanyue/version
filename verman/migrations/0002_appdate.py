# Generated by Django 2.1.1 on 2018-10-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=50)),
                ('adnroid', models.CharField(max_length=50)),
                ('ios', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('test_account', models.CharField(max_length=50)),
                ('user_add', models.CharField(blank=True, help_text='添加用户', max_length=50)),
            ],
        ),
    ]
