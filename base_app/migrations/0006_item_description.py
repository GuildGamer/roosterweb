# Generated by Django 3.0.5 on 2020-05-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='i am a description hooray'),
            preserve_default=False,
        ),
    ]
