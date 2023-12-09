# Generated by Django 5.0 on 2023-12-09 16:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.PositiveSmallIntegerField(choices=[(1, 'Too bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='comic.comic')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
                'unique_together': {('user_id', 'comic_id')},
            },
        ),
    ]
