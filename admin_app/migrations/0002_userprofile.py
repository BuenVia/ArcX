# Generated by Django 5.1.1 on 2024-11-09 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=45, null=True)),
                ('address_one', models.CharField(blank=True, max_length=45, null=True)),
                ('address_two', models.CharField(blank=True, max_length=45, null=True)),
                ('town', models.CharField(blank=True, max_length=45, null=True)),
                ('county', models.CharField(blank=True, max_length=45, null=True)),
                ('postcode', models.CharField(blank=True, max_length=15, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
