# Generated by Django 2.0.6 on 2019-05-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0005_auto_20190506_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='group1',
            name='negative_opening',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='group1',
            name='positive_opening',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]