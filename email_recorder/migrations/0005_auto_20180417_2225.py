# Generated by Django 2.0.3 on 2018-04-17 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_recorder', '0004_elist_heavylist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='elist',
            new_name='liststore',
        ),
    ]
