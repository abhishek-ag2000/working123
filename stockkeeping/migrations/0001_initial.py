# Generated by Django 2.0.6 on 2019-05-03 06:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting_double_entry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compoundunits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('conversion', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
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
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('Party_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partyledger', to='accounting_double_entry.ledger1')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseledger', to='accounting_double_entry.ledger1')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_no', models.PositiveIntegerField()),
                ('billname', models.CharField(default='Customer', max_length=32)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
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
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('Party_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partyledgersales', to='accounting_double_entry.ledger1')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saleledger', to='accounting_double_entry.ledger1')),
            ],
        ),
        migrations.CreateModel(
            name='Simpleunits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol', models.CharField(max_length=32)),
                ('formal', models.CharField(max_length=32)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='stock_journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('opening_stock', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('closing_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('closing_stock', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_closing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity_p', models.PositiveIntegerField(default=0)),
                ('rate_p', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('Disc_p', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('gst_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('ugst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('cgst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Total_p', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('purchases', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasetotal', to='stockkeeping.Purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Total_sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('Disc', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('gst_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('ugst', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5)),
                ('cgst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gst_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('sales', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saletotal', to='stockkeeping.Sales')),
            ],
        ),
        migrations.CreateModel(
            name='Stockdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('opening', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock_name', models.CharField(max_length=32)),
                ('batch_no', models.PositiveIntegerField(blank=True, null=True)),
                ('bar_code', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='stockmanagement')),
                ('mnf_date', models.DateField(blank=True, null=True)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('gst_rate', models.DecimalField(decimal_places=2, default=5, max_digits=4)),
                ('hsn', models.PositiveIntegerField()),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_stock', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stockgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True, null=True)),
                ('urlhash', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=32)),
                ('quantities', models.BooleanField(default=False)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('under', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stock_group', to='stockkeeping.Stockgroup')),
            ],
        ),
        migrations.AddField(
            model_name='stockdata',
            name='under',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stockkeeping.Stockgroup'),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='unitcomplex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seconds_unit_complex', to='stockkeeping.Compoundunits'),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='unitsimple',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firsts_unit', to='stockkeeping.Simpleunits'),
        ),
        migrations.AddField(
            model_name='stock_total_sales',
            name='stockitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salestock', to='stockkeeping.Stockdata'),
        ),
        migrations.AddField(
            model_name='stock_total',
            name='stockitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasestock', to='stockkeeping.Stockdata'),
        ),
        migrations.AddField(
            model_name='stock_journal',
            name='stockitem',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closingstock', to='stockkeeping.Stockdata'),
        ),
        migrations.AddField(
            model_name='compoundunits',
            name='firstunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firsts', to='stockkeeping.Simpleunits'),
        ),
        migrations.AddField(
            model_name='compoundunits',
            name='seconds_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seconds', to='stockkeeping.Simpleunits'),
        ),
    ]