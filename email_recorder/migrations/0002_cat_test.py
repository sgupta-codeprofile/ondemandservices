# Generated by Django 2.0.3 on 2018-04-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_recorder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='test',
            field=models.CharField(default='none by user', max_length=100),
        ),
    ]
