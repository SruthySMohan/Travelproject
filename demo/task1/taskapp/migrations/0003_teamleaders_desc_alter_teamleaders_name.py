# Generated by Django 4.0.6 on 2022-07-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_teamleaders'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamleaders',
            name='desc',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teamleaders',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]