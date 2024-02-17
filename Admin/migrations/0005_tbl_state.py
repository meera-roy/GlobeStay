# Generated by Django 5.0 on 2023-12-30 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_delete_tbl_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_country')),
            ],
        ),
    ]
