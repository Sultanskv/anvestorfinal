# Generated by Django 5.0.6 on 2024-07-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_trade_quantity_remove_trade_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='lot_size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='clint_id',
            field=models.CharField(default='fc31df06', max_length=8, unique=True),
        ),
    ]
