# Generated by Django 4.0.4 on 2022-06-17 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leaf', '0006_productousuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cont_cant',
        ),
    ]