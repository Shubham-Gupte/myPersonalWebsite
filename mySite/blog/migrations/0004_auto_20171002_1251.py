# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/blog/img'),
        ),
    ]
