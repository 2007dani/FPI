# Generated by Django 3.1.5 on 2021-09-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPPI', '0012_auto_20210908_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
        migrations.AlterField(
            model_name='dather',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
        migrations.AlterField(
            model_name='father',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
        migrations.AlterField(
            model_name='mother',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
        migrations.AlterField(
            model_name='sister',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
        migrations.AlterField(
            model_name='son',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
        migrations.AlterField(
            model_name='souse',
            name='Birth',
            field=models.CharField(max_length=100, null=1),
        ),
    ]