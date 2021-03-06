# Generated by Django 2.2 on 2020-03-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_goods_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='type',
            field=models.IntegerField(choices=[(0, '条码打印机'), (1, '条码扫描器'), (2, '数据终端'), (3, '软件'), (4, '配件'), (5, '耗材'), (6, 'RFID设备'), (7, '其它')], default=0, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='unit',
            field=models.IntegerField(choices=[(0, '台'), (1, '支'), (2, '个'), (3, '站点'), (4, '用户'), (5, '套'), (6, 'PCS')], default=0, verbose_name='单位'),
        ),
    ]
