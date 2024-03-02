# Generated by Django 5.0 on 2024-03-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_tbl_userrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=50)),
                ('feedbackdate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='tbl_userrating',
            old_name='rent',
            new_name='reant',
        ),
    ]
