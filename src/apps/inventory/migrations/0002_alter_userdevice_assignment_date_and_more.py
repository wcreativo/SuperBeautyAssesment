# Generated by Django 5.0.1 on 2024-02-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdevice',
            name='assignment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdevice',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
