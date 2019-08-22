# Generated by Django 2.0.6 on 2019-08-17 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qr_code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemasterqr',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Company_employee', to='company.Organisation'),
        ),
        migrations.AlterField(
            model_name='stockmasterqr',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Company_stock_master', to='company.Organisation'),
        ),
    ]
