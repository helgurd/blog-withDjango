# Generated by Django 3.0.2 on 2020-06-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thum',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
