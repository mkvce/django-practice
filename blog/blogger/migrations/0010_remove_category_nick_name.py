# Generated by Django 3.1.6 on 2021-03-03 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0009_category_nick_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nick_name',
        ),
    ]