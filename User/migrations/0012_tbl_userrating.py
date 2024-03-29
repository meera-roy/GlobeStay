# Generated by Django 5.0 on 2024-03-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_tbl_usercomplaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userrating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_data', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('user_review', models.CharField(max_length=50)),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
