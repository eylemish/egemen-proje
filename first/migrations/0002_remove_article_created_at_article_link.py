# Generated by Django 5.1.5 on 2025-01-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
