# Generated by Django 5.0 on 2024-01-04 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0012_tbl_subadminregistration'),
        ('Guest', '0004_delete_tbl_ownerregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ownerregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='MemberDocs/')),
                ('proof', models.FileField(upload_to='MemberDocs/')),
                ('password', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
