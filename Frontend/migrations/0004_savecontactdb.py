# Generated by Django 4.1.4 on 2023-01-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_remove_registrationdb_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='savecontactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=30, null=True)),
                ('Subject', models.CharField(blank=True, max_length=30, null=True)),
                ('Message', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]