# Generated by Django 2.2.24 on 2021-12-26 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0003_neighbourhood_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='admin',
        ),
    ]
