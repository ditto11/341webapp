# Generated by Django 2.2.12 on 2020-12-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201130_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=650),
        ),
    ]