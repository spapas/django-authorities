# Generated by Django 3.0.7 on 2020-06-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorities', '0002_auto_20200224_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]