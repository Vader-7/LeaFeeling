# Generated by Django 4.0.4 on 2022-06-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leaf', '0004_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cont_cant',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]