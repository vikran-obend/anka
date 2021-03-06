# Generated by Django 2.2.2 on 2019-06-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20190620_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_number', models.IntegerField()),
                ('news_event', models.TextField(max_length=500)),
                ('news_class', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Upcoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=25)),
                ('event', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
