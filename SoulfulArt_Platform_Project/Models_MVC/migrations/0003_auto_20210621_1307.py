# Generated by Django 3.1.7 on 2021-06-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models_MVC', '0002_auto_20210618_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_street_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]