# Generated by Django 3.2.5 on 2021-11-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0017_auto_20211108_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='data',
            new_name='Data',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='metadata',
            new_name='Metadata',
        ),
    ]