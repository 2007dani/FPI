# Generated by Django 3.2.1 on 2021-09-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0007_person_moreinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='MoreInfo',
            field=models.CharField(max_length=3000, null=1),
        ),
    ]
