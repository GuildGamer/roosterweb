# Generated by Django 3.0.5 on 2020-05-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_auto_20200511_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('B', 'Bestseller'), ('S', 'Special Deal')], max_length=1),
        ),
    ]
