# Generated by Django 4.2.3 on 2023-07-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]