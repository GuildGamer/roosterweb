# Generated by Django 3.0.5 on 2020-06-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0018_auto_20200618_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('N', 'New'), ('B', 'Bestseller'), ('S', 'Special Deal')], max_length=1, null=True),
        ),
    ]