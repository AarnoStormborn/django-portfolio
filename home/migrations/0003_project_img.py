# Generated by Django 4.0.6 on 2022-08-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_decsription_specialskills_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(default='image1.jpg', upload_to='project_images'),
        ),
    ]
