# Generated by Django 4.0.4 on 2022-05-20 16:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receita', '0002_alter_receita_date_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 20, 13, 53, 52, 413313)),
        ),
    ]