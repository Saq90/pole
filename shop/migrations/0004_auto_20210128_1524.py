# Generated by Django 2.1.13 on 2021-01-28 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210123_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
