# Generated by Django 2.2.2 on 2019-06-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_news_news_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_class',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
