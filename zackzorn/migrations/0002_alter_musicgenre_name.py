# Generated by Django 3.2.9 on 2021-11-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zackzorn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicgenre',
            name='name',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]
