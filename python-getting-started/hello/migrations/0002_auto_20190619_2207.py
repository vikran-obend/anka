# Generated by Django 2.2.2 on 2019-06-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upcoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=25)),
                ('event', models.TextField(max_length=500)),
                ('location', models.TextField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]