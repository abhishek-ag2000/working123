# Generated by Django 2.0.6 on 2019-08-20 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190819_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static_page/portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title1', models.TextField(blank=True, null=True)),
                ('title2', models.TextField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('service_desc', models.TextField(blank=True, null=True)),
                ('portfolio_desc', models.TextField(blank=True, null=True)),
                ('team_desc', models.TextField(blank=True, null=True)),
                ('head_bg', models.ImageField(blank=True, null=True, upload_to='static_page/head_img')),
                ('organisation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_static_page', to='company.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='static_page/team')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('staticpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='static_page_teammember', to='company.StaticPage')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='staticpage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='static_page_service', to='company.StaticPage'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='staticpage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='static_page_portfolio', to='company.StaticPage'),
        ),
    ]
