# Generated by Django 3.2.6 on 2021-08-23 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0002_auto_20210822_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='vote_score',
        ),
    ]
