# Generated by Django 2.2.12 on 2020-12-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20201130_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=350),
        ),
    ]
