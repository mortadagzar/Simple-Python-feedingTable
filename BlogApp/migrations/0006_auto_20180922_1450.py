# Generated by Django 2.1.1 on 2018-09-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_qoute_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qoute',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]