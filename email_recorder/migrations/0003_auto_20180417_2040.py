# Generated by Django 2.0.3 on 2018-04-17 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_recorder', '0002_cat_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='usr_cat',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='elist',
            old_name='usr_list',
            new_name='cat',
        ),
    ]
