# Generated by Django 2.1.1 on 2018-09-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0024_auto_20180926_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userkhan',
            name='hisemail',
        ),
        migrations.AddField(
            model_name='qoute',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='qoute',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='qoute',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
