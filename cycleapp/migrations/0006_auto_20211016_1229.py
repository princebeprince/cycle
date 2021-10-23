# Generated by Django 3.2.8 on 2021-10-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapp', '0005_cycles_model_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycles',
            name='frame_desc',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cycles',
            name='gear_desc',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cycles',
            name='tyre_desc',
            field=models.CharField(default='', max_length=250),
        ),
    ]