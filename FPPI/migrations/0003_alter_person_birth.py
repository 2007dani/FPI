# Generated by Django 3.2.1 on 2021-08-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0002_alter_person_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
    ]