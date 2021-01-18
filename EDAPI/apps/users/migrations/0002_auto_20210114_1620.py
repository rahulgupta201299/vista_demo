# Generated by Django 3.1.5 on 2021-01-14 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='PIN_CODE',
            field=models.CharField(default=123, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]