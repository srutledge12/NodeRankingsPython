# Generated by Django 3.2.5 on 2021-11-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0011_auto_20211107_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedata',
            name='URL',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
