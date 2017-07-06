# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ST', models.CharField(max_length=2, verbose_name=b'State', validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{2}$', message=b'State must be 2 capital letters', code=None)])),
                ('city', models.CharField(max_length=60, verbose_name=b'City')),
                ('lat', models.DecimalField(verbose_name=b'Latitude', max_digits=9, decimal_places=6)),
                ('lng', models.DecimalField(verbose_name=b'Longitude', max_digits=9, decimal_places=6)),
                ('pop', models.IntegerField(default=0, verbose_name=b'Population')),
            ],
        ),
    ]
