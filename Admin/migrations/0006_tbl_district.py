# Generated by Django 5.0 on 2023-12-30 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_state')),
            ],
        ),
    ]
