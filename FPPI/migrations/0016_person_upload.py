# Generated by Django 3.1.5 on 2021-10-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0015_auto_20210913_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='upload',
            field=models.ImageField(null=1, upload_to='uploads/'),
            preserve_default=1,
        ),
    ]