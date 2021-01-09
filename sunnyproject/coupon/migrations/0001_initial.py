# Generated by Django 3.1.4 on 2021-01-04 21:46

import coupon.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='TITLE')),
                ('image', coupon.fields.CouponImageField(upload_to='photo/%Y/%m')),
                ('upload_dt', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
            ],
        ),
    ]
