# Generated by Django 2.2.6 on 2019-11-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191126_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='list_tags', to='app.Tag'),
        ),
    ]
