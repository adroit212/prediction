# Generated by Django 3.0.8 on 2020-07-26 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='passsword',
            new_name='password',
        ),
    ]
