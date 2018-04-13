# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(max_digits=8, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=80)),
                ('value_type', models.CharField(default=b'v', max_length=1, choices=[(b'i', 'Integer'), (b'f', 'Float'), (b'b', 'Boolean')])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='reading',
            name='sensor',
            field=models.ForeignKey(to='sensors.Sensor'),
        ),
    ]
