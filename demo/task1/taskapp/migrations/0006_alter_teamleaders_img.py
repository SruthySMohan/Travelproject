# Generated by Django 4.0.6 on 2022-07-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0005_alter_teamleaders_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleaders',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
