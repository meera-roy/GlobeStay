# Generated by Django 5.0 on 2023-12-30 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_delete_tbl_subadminregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subadminregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('photo', models.FileField(upload_to='MemberDocs/')),
                ('password', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_country')),
            ],
        ),
    ]
