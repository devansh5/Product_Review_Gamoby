# Generated by Django 3.0.4 on 2020-03-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20200328_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
