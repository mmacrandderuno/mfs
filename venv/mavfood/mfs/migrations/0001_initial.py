# Generated by Django 2.1.5 on 2019-02-04 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('custemail', models.CharField(max_length=255)),
                ('custphone', models.CharField(max_length=10)),
                ('custorg', models.CharField(max_length=100)),
                ('custrole', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('custbldgroom', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=6)),
                ('notes', models.TextField()),
                ('custadd_date', models.DateTimeField(blank=True, null=True)),
                ('custupdate_date', models.DateTimeField(blank=True, null=True)),
                ('custupdateby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('productdesc', models.TextField()),
                ('productquantity', models.IntegerField()),
                ('pickupdate', models.DateField()),
                ('pickuptime', models.TimeField(null=True)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=15)),
                ('prodadd_date', models.DateTimeField(blank=True, null=True)),
                ('produpdate_date', models.DateTimeField(blank=True, null=True)),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mfs.Cust')),
                ('produpdateby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicecategory', models.CharField(max_length=100)),
                ('servicedesc', models.TextField()),
                ('servicelocation', models.CharField(max_length=100)),
                ('servicedate', models.DateField()),
                ('setuptime', models.TimeField()),
                ('cleanuptime', models.TimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=15)),
                ('servadd_date', models.DateTimeField(blank=True, null=True)),
                ('servupdate_date', models.DateTimeField(blank=True, null=True)),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mfs.Cust')),
                ('servupdateby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
