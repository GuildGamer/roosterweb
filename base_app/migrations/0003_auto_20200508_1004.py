# Generated by Django 3.0.5 on 2020-05-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20200508_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('MF', "Men's Fashion"), ('WF', "Women's Fashion"), ('CJ', 'Clothing and Jewelry'), ('FO', 'Food'), ('WD', 'Web & Mobile Development'), ('AS', 'Art and Stationary')], max_length=2),
        ),
    ]
