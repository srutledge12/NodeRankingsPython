# Generated by Django 3.2.5 on 2021-11-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0015_remove_packagedata_registry_packagedata_content_or_url'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='packagedata',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('Content__isnull', False), ('URL__isnull', True)), models.Q(('Content__isnull', True), ('URL__isnull', False)), _connector='OR'), name='registry_packagedata_content_or_url'),
        ),
    ]
