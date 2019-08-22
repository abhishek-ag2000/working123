# Generated by Django 2.0.6 on 2019-08-19 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bracketline', '0002_initial_data'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(blank=True)),
                ('url_hash', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('address', models.TextField(blank=True)),
                ('telephone_no', models.CharField(blank=True, max_length=32, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=32, null=True)),
                ('country', models.ForeignKey(default=12, on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_country', to='bracketline.CountryMaster')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_state', to='bracketline.StateMaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisation_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.RemoveField(
            model_name='company',
            name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='company',
            name='state',
        ),
        migrations.RemoveField(
            model_name='company',
            name='telephone_no',
        ),
        migrations.AddField(
            model_name='company',
            name='organisation',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_organisation', to='company.Organisation'),
            preserve_default=False,
        ),
    ]
