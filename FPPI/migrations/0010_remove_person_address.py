# Generated by Django 3.2.1 on 2021-09-07 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0009_person_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Address',
        ),
    ]