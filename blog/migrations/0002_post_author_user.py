# Generated by Django 4.2.4 on 2023-11-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_user',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
