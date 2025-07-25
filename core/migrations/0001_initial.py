# Generated by Django 5.2.4 on 2025-07-03 18:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=7)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.language')),
                ('saved_by', models.ManyToManyField(blank=True, related_name='saved_snippets', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='core.tag')),
            ],
        ),
    ]
