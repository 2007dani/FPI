# Generated by Django 3.2.1 on 2021-08-29 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0005_alter_person_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Image',
        ),
    ]