# Generated by Django 5.0 on 2024-02-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_tbl_userrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_userrequest',
            name='fromdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_userrequest',
            name='todate',
            field=models.DateField(),
        ),
    ]