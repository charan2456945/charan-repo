# Generated by Django 3.2.3 on 2021-05-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0002_auto_20210316_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
