# Generated by Django 2.1.1 on 2018-09-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0017_auto_20180924_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qoute',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qoute',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]