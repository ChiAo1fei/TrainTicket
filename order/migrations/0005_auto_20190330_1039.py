# Generated by Django 2.1.7 on 2019-03-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20190330_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_alter',
            field=models.BooleanField(choices=[('0', '否'), ('1', '是')], default=0, verbose_name='是否改签'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_delete',
            field=models.BooleanField(choices=[('0', '否'), ('1', '是')], default=0, verbose_name='是否退票'),
        ),
    ]
