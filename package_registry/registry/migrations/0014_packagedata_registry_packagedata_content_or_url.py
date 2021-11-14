# Generated by Django 3.2.5 on 2021-11-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0013_alter_packagedata_content'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='packagedata',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('Content__isnull', True), ('URL__isnull', False)), models.Q(('Content__isnull', False), ('URL__isnull', True)), _connector='OR'), name='registry_packagedata_Content_or_URL'),
        ),
    ]