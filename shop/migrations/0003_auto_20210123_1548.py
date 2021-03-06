# Generated by Django 2.1.13 on 2021-01-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
