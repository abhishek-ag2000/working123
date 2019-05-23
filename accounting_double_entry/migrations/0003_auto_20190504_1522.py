# Generated by Django 2.0.6 on 2019-05-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0002_auto_20190503_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger1',
            name='To_pl_credit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ledger1',
            name='To_pl_debit',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]