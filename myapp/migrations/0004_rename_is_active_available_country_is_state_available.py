# Generated by Django 5.0.6 on 2024-07-09 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_is_state_available_country_is_active_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='is_active_available',
            new_name='is_state_available',
        ),
    ]
