# Generated by Django 4.0.6 on 2022-08-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialskills',
            old_name='decsription',
            new_name='description',
        ),
    ]
