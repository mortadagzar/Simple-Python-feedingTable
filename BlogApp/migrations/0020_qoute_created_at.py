# Generated by Django 2.1.1 on 2018-09-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0019_remove_qoute_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoute',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]