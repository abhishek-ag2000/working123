# Generated by Django 2.0.6 on 2019-06-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpandsupport', '0002_helpcategories_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
