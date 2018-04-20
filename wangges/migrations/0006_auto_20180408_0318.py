# Generated by Django 2.0.2 on 2018-04-08 03:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wangges', '0005_stockcode_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZXG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
        migrations.AlterField(
            model_name='stockcode',
            name='code',
            field=models.CharField(db_index=True, max_length=10, unique=True, verbose_name='代码'),
        ),
        migrations.AddField(
            model_name='zxg',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wangges.Stockcode'),
        ),
    ]