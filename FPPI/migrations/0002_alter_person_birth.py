# Generated by Django 3.2.1 on 2021-08-23 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Birth',
            field=models.DateTimeField(null=1),
        ),
    ]
