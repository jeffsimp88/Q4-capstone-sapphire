# Generated by Django 3.1.7 on 2021-04-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0002_net_moderators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='net',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
