# Generated by Django 3.2.5 on 2021-09-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_bartender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title_c',
            field=models.CharField(max_length=20, unique=True, verbose_name='Title of category'),
        ),
    ]
