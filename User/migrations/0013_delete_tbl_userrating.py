# Generated by Django 5.0 on 2024-03-02 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_tbl_userrating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_userrating',
        ),
    ]