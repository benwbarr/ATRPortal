# Generated by Django 3.2.8 on 2021-11-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0004_auto_20211105_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='rdate',
            field=models.DateTimeField(verbose_name='Receiving Date'),
        ),
    ]
