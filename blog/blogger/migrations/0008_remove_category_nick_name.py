# Generated by Django 3.1.6 on 2021-03-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0007_auto_20210303_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nick_name',
        ),
    ]
