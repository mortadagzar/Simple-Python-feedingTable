# Generated by Django 2.1.1 on 2018-09-22 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_article_article_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
    ]