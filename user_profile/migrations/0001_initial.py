# Generated by Django 2.0.6 on 2019-08-14 11:10

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce_integration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bracketline', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_case', models.BooleanField(default=False)),
                ('act', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('facts', models.CharField(blank=True, max_length=100)),
                ('issue', models.CharField(blank=True, max_length=100)),
                ('argument', models.CharField(blank=True, max_length=100)),
                ('judgement', models.CharField(blank=True, max_length=100)),
                ('user_role', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like', models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='user_profile.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductActivated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('is_active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_activate', to='ecommerce_integration.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=100)),
                ('details', models.CharField(blank=True, max_length=100)),
                ('service_type', models.CharField(blank=True, choices=[('Returns', 'Returns'), ('Communication', 'Communication'), ('License', 'License')], default='Returns', max_length=100)),
                ('duration', models.CharField(blank=True, choices=[('ANNUALLY', 'ANNUALLY'), ('QUARTERLY', 'QUARTERLY'), ('ONE TIME', 'ONE TIME')], default='ANNUALLY', max_length=100)),
                ('service_mode', models.CharField(blank=True, choices=[('ON-PREMISES', 'ON-PREMISES'), ('CALLS - VOIP', 'CALLS - VOIP'), ('COLLECTION FROM CLIENT', 'COLLECTION FROM CLIENT')], default='ON-PREMISES', max_length=100)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalVerify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.BigIntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('upload_1', models.FileField(blank=True, upload_to='pro_verification', validators=[user_profile.models.file_size])),
                ('u1_status', models.BooleanField(default=False)),
                ('upload_2', models.FileField(blank=True, upload_to='pro_verification', validators=[user_profile.models.file_size])),
                ('u2_status', models.BooleanField(default=False)),
                ('upload_3', models.FileField(blank=True, upload_to='pro_verification', validators=[user_profile.models.file_size])),
                ('u3_status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_product', to='ecommerce_integration.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(blank=True, max_length=32)),
                ('user_type', models.CharField(choices=[('Bussiness user', 'Bussiness user'), ('Professional', 'Professional'), ('Data Operators', 'Data Operators'), ('Others', 'Others')], default='Others', max_length=32)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('permanent_address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('phone_no', models.CharField(blank=True, max_length=32)),
                ('basic_info', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='user_images')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_country', to='bracketline.CountryMaster')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_state', to='bracketline.StateMaster')),
                ('subscribed_products', models.ManyToManyField(blank=True, related_name='products_subscribed', to='ecommerce_integration.Product')),
                ('subscribed_role_products', models.ManyToManyField(blank=True, related_name='role_products_subscribed', to='ecommerce_integration.RoleBasedProduct')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoleBasedProductActivated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('is_active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_product_activate', to='ecommerce_integration.RoleBasedProduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
