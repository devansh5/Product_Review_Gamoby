# Generated by Django 3.0.4 on 2020-03-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20200328_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(default='2', primary_key=True, serialize=False),
        ),
    ]