# Generated by Django 5.0 on 2024-02-25 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_tbl_complainttype'),
        ('Guest', '0008_tbl_ownerregistration_status'),
        ('Owner', '0009_delete_tbl_ownercomplaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ownercomplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complainttitle', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('complaintdate', models.DateField(auto_now_add=True)),
                ('complaint_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_complainttype')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_ownerregistration')),
            ],
        ),
    ]
