# Generated by Django 2.2.24 on 2021-12-28 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0016_auto_20211228_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='owner',
            new_name='user',
        ),
    ]
