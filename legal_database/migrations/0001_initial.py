# Generated by Django 2.0.6 on 2019-09-09 14:10

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('bare_body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('facts', models.TextField(blank=True, null=True)),
                ('issues', models.TextField(blank=True, null=True)),
                ('ratio', models.TextField(blank=True, null=True)),
                ('arguments', models.TextField(blank=True, null=True)),
                ('judgement', models.TextField(blank=True, null=True)),
                ('critics', models.TextField(blank=True, null=True)),
                ('court', models.CharField(blank=True, max_length=100, null=True)),
                ('sitations', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Forex & Banking', 'Forex & Banking'), ('Capital Market', 'Capital Market'), ('Corporate Laws', 'Corporate Laws'), ('Competition Laws', 'Competition Laws'), ('Indirect Taxation', 'Indirect Taxation'), ('Direct Taxation', 'Direct Taxation'), ('VAT', 'VAT'), ('Sales Tax', 'Sales Tax'), ('Compliance Almanac', 'Compliance Almanac'), ('Employment Laws', 'Employment Laws'), ('Labour', 'Labour'), ('Criminal Laws', 'Criminal Laws'), ('Insurance', 'Insurance'), ('Industrial & Service', 'Industrial & Service'), ('Human Rights', 'Human Rights'), ('Foreign Trade Policy', 'Foreign Trade Policy'), ('Indian Industrial Policy', 'Indian Industrial Policy'), ('Environment', 'Environment'), ('Intellectual Property Rights', 'Intellectual Property Rights'), ('Cyber & IT Laws', 'Cyber & IT Laws'), ('Media & Communication', 'Media & Communication'), ('Anti-Dumping', 'Anti-Dumping'), ('WTO', 'WTO'), ('Power & Energy', 'Power & Energy'), ('Mines & Minerals', 'Mines & Minerals')], default='Forex & Banking', max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CentralBareAct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('bare_body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('cases', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_acts_cases', to='legal_database.Cases')),
                ('categories', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_acts', to='legal_database.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('title', models.TextField(blank=True)),
                ('central_act', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_acts_chap', to='legal_database.CentralBareAct')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('sitations', models.TextField(blank=True)),
                ('cases', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_cases', to='legal_database.Cases')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_category', to='legal_database.Categories')),
                ('central_act', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_acts_noti', to='legal_database.CentralBareAct')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('sitations', models.TextField(blank=True)),
                ('cases', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_cases', to='legal_database.Cases')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_category', to='legal_database.Categories')),
                ('central_act', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_acts_order', to='legal_database.CentralBareAct')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('title', models.TextField(blank=True, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('citations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('cases', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_cases', to='legal_database.Cases')),
                ('central_act', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_acts_sec', to='legal_database.CentralBareAct')),
                ('chapter', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='legal_database.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='StateBareAct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('bare_body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('cases', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sb_acts_cases', to='legal_database.Cases')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sb_acts', to='legal_database.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('sitations', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('section', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='legal_database.Section')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='state_act',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sb_acts_sec', to='legal_database.StateBareAct'),
        ),
        migrations.AddField(
            model_name='order',
            name='state_act',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sb_acts_order', to='legal_database.StateBareAct'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='state_act',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sb_acts_noti', to='legal_database.StateBareAct'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='state_act',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sb_acts_chap', to='legal_database.StateBareAct'),
        ),
        migrations.AddField(
            model_name='cases',
            name='categories',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Case_cat', to='legal_database.Categories'),
        ),
    ]
