# Generated by Django 2.1.1 on 2018-09-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0021_auto_20180925_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qoute',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='qoute',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]