# Generated by Django 2.2.12 on 2020-12-01 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20201130_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=760),
        ),
    ]
