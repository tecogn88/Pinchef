# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20150302_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(max_length=11)),
                ('usuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
