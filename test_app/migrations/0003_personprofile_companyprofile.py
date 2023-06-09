# Generated by Django 4.1.7 on 2023-03-24 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_app_company_job_person_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_app.company')),
            ],
        ),
    ]
