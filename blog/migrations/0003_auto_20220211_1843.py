# Generated by Django 2.2.5 on 2022-02-11 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220211_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'verbose_name': 'آی\u200cپی', 'verbose_name_plural': 'آی\u200cپی ها'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]
