# Generated by Django 3.2.8 on 2021-11-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0007_alter_activity_jobnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='jobnumber',
            field=models.CharField(max_length=120, verbose_name='Job Number'),
        ),
    ]