# Generated by Django 3.1.1 on 2020-10-12 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201012_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 14, 45, 20, 446099), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='TutorialCategory',
        ),
        migrations.DeleteModel(
            name='TutorialSeries',
        ),
    ]
