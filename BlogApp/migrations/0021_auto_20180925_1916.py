# Generated by Django 2.1.1 on 2018-09-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0020_qoute_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qoute',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]