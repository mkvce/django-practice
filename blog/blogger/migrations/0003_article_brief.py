# Generated by Django 3.1.6 on 2021-02-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_auto_20210206_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='brief',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
