# Generated by Django 3.2 on 2022-06-18 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0024_auto_20220618_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='area_administrator',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='health_tell',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='police_number',
        ),
    ]
