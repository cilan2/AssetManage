# Generated by Django 2.2 on 2019-12-04 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20191204_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverport',
            name='SID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.ServerS', verbose_name='Server序列号'),
        ),
    ]
