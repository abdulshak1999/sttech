# Generated by Django 3.1.8 on 2021-05-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210514_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='object_id',
        ),
        migrations.AddField(
            model_name='notification',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
