# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text=b'First Name', max_length=15)),
                ('last_name', models.CharField(help_text=b'Last Name', max_length=15)),
                ('date_of_birth', models.DateField(help_text=b'Date Of Birth')),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('email', models.EmailField(help_text=b'Email address', max_length=100)),
                ('password', models.CharField(help_text=b'password', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
