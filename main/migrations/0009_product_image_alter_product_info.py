# Generated by Django 4.1 on 2022-11-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_substitute_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(related_name='image', to='main.detail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='info',
            field=models.ManyToManyField(related_name='info', to='main.detail'),
        ),
    ]