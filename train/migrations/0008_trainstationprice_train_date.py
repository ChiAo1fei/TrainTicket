# Generated by Django 2.1.7 on 2019-04-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0007_auto_20190330_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainstationprice',
            name='train_date',
            field=models.DateField(null=True, verbose_name='运行日期'),
        ),
    ]
