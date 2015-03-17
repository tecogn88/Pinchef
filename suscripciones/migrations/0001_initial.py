# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_cliente', models.CharField(max_length=25)),
                ('id_suscripcion', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=15)),
                ('activo', models.BooleanField(default=False)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Suscripci\xf3n',
                'verbose_name_plural': 'Suscripciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='log',
            name='suscripcion',
            field=models.ForeignKey(related_name='logs', to='suscripciones.Suscripcion'),
            preserve_default=True,
        ),
    ]
