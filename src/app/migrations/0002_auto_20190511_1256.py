# Generated by Django 2.2.1 on 2019-05-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonaccicheck',
            name='numeric',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fibonaccicheck',
            name='output',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
