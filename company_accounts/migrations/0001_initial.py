# Generated by Django 2.0.6 on 2019-05-03 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting_double_entry', '0001_initial'),
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('ref_no', models.PositiveIntegerField()),
                ('billname', models.CharField(default='Supplier', max_length=32)),
                ('Address', models.CharField(blank=True, max_length=32)),
                ('GSTIN', models.CharField(blank=True, max_length=32)),
                ('PAN', models.CharField(blank=True, max_length=32)),
                ('State', models.CharField(choices=[('Choose', 'Choose'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi '), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Choose', max_length=100)),
                ('Contact', models.BigIntegerField(blank=True, null=True)),
                ('DeliveryNote', models.CharField(blank=True, max_length=32)),
                ('Supplierref', models.CharField(blank=True, max_length=32)),
                ('Mode', models.TextField(blank=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cgst_alltotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst_alltotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Companypurchase_account', to='company.company')),
                ('Party_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partyledger_account', to='accounting_double_entry.ledger1')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Userpurchase_account', to=settings.AUTH_USER_MODEL)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseledger_account', to='accounting_double_entry.ledger1')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity_p', models.PositiveIntegerField(default=0)),
                ('rate_p', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('gst_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('Disc_p', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('ugst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('cgst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Total_p', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('purchase_ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasestock_accounts', to='accounting_double_entry.ledger1')),
                ('purchases', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasetotal_accounts', to='company_accounts.Purchase_accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Sales_accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_no', models.PositiveIntegerField()),
                ('billname', models.CharField(default='Customer', max_length=32)),
                ('date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('Address', models.CharField(blank=True, max_length=32)),
                ('GSTIN', models.CharField(blank=True, max_length=32)),
                ('PAN', models.CharField(blank=True, max_length=32)),
                ('State', models.CharField(choices=[('Choose', 'Choose'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi '), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Choose', max_length=100)),
                ('Contact', models.BigIntegerField(blank=True, null=True)),
                ('DeliveryNote', models.CharField(blank=True, max_length=32)),
                ('Supplierref', models.CharField(blank=True, max_length=32)),
                ('Mode', models.TextField(blank=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cgst_alltotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst_alltotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Companysales_account', to='company.company')),
                ('Party_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partyledgersales_account', to='accounting_double_entry.ledger1')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Usersales_account', to=settings.AUTH_USER_MODEL)),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saleledger_account', to='accounting_double_entry.ledger1')),
            ],
        ),
        migrations.CreateModel(
            name='Sales_total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('gst_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('Disc', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('ugst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('cgst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('sales', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saletotal_accounts', to='company_accounts.Sales_accounts')),
                ('sales_ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salestock_accounts', to='accounting_double_entry.ledger1')),
            ],
        ),
    ]