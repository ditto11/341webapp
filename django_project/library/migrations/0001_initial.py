# Generated by Django 2.2.12 on 2020-12-01 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=50)),
                ('publisheddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('libraryid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=50)),
                ('streetaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('patronid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('phonenumber', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('libraryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Library')),
            ],
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('dateplaced', models.DateField()),
                ('holdid', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('libraryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Library')),
                ('patronid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Patron')),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('copynumber', models.IntegerField(default=0)),
                ('purchasedate', models.DateField()),
                ('condition', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('copyid', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('libraryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Library')),
            ],
        ),
        migrations.CreateModel(
            name='CheckedOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copynumber', models.IntegerField(default=0)),
                ('checkoutdate', models.DateField()),
                ('duedate', models.DateField()),
                ('timesrenewed', models.IntegerField(default=0)),
                ('overduefee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('copyid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='library.Copy')),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('patronid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Patron')),
            ],
        ),
    ]
