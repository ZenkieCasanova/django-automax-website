# Generated by Django 4.2.7 on 2023-12-07 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]
