# Generated by Django 5.0.6 on 2024-07-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_admin', '0012_alter_sub_admindt_subadmin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_admindt',
            name='subadmin_id',
            field=models.CharField(default='d5e910bf', max_length=8, unique=True),
        ),
    ]