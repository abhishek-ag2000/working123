# Generated by Django 2.0.6 on 2019-05-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group1',
            name='Total_Credit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='group1',
            name='Total_Debit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ledger1',
            name='Total_Credit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ledger1',
            name='Total_Debit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
