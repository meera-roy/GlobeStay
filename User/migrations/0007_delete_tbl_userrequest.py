# Generated by Django 5.0 on 2024-02-18 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_tbl_userrequest_fromdate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_userrequest',
        ),
    ]