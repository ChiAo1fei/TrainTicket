# Generated by Django 2.1.7 on 2019-03-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0004_auto_20190330_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traininfo',
            name='train_type',
            field=models.CharField(choices=[('C', '城际列车'), ('D', '动车组'), ('G', '高速列车'), ('Z', '直达列车'), ('T', '特快列车'), ('K', '快速列车'), ('L', '临时旅客列车'), ('A', '局管内临时旅客列车'), ('Y', '旅游列车')], max_length=1, null=True, verbose_name='火车类型'),
        ),
    ]
