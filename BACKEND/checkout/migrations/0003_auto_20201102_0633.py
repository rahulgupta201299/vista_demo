# Generated by Django 3.1.2 on 2020-11-02 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20201102_0328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pay',
            old_name='buyer',
            new_name='user',
        ),
    ]
