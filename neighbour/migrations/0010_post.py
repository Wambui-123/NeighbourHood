# Generated by Django 2.2.24 on 2021-12-28 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbour', '0009_auto_20211228_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='neighbour.NeighbourHood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]