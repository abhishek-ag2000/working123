# Generated by Django 2.0.6 on 2019-08-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_entry', '0004_auto_20190822_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgermaster',
            name='assessable_value',
            field=models.CharField(blank=True, choices=[('Not Applicable', 'Not Applicable'), ('GST', 'GST')], default='Not Applicable', max_length=20),
        ),
        migrations.AlterField(
            model_name='ledgermaster',
            name='duty_tax_type',
            field=models.CharField(blank=True, choices=[('Others', 'Others'), ('GST', 'GST')], default='Others', max_length=10),
        ),
        migrations.AlterField(
            model_name='ledgermaster',
            name='gst_applicable',
            field=models.CharField(blank=True, choices=[('Applicable', 'Applicable'), ('Not Applicable', 'Not Applicable'), ('Undefined', 'Undefined')], default='Not Applicable', max_length=20),
        ),
        migrations.AlterField(
            model_name='ledgermaster',
            name='registration_type',
            field=models.CharField(blank=True, choices=[('Unknown', 'Unknown'), ('Composition', 'Composition'), ('Consumer', 'Consumer'), ('Regular', 'Regular'), ('Unregistered', 'Unregistered')], default='Unregistered', max_length=20),
        ),
        migrations.AlterField(
            model_name='ledgermaster',
            name='set_or_alter_gst',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='ledgermaster',
            name='set_or_alter_gst_tax',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='ledgermaster',
            name='supply_type',
            field=models.CharField(blank=True, choices=[('Goods', 'Goods'), ('Services', 'Services')], default='Goods', max_length=10),
        ),
    ]