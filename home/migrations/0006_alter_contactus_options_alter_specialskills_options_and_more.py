# Generated by Django 4.0.6 on 2022-08-13 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_decsription_project_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='specialskills',
            options={'verbose_name_plural': 'Special Skills'},
        ),
        migrations.AlterModelOptions(
            name='workexp',
            options={'verbose_name_plural': 'Work Experience'},
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='context',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='phone',
            new_name='message',
        ),
    ]
