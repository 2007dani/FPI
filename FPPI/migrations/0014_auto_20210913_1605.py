# Generated by Django 3.1.5 on 2021-09-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0013_auto_20210912_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brother',
            name='Person',
        ),
        migrations.RemoveField(
            model_name='sister',
            name='Person',
        ),
        migrations.RemoveField(
            model_name='souse',
            name='Person',
        ),
        migrations.AddField(
            model_name='person',
            name='Brother',
            field=models.ManyToManyField(null=1, to='FPPI.Brother'),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='person',
            name='Sister',
            field=models.ManyToManyField(null=1, to='FPPI.Sister'),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='person',
            name='Souse',
            field=models.ManyToManyField(null=1, to='FPPI.Souse'),
            preserve_default=1,
        ),
    ]