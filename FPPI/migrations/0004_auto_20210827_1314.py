# Generated by Django 3.2.1 on 2021-08-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0003_alter_person_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='father',
            old_name='Person_id',
            new_name='person_id',
        ),
        migrations.RenameField(
            model_name='mother',
            old_name='Person_id',
            new_name='person_id',
        ),
        migrations.AddField(
            model_name='person',
            name='Image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
