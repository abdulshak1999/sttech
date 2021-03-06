# Generated by Django 3.1.8 on 2021-05-14 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0005_auto_20210514_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='id',
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='object_id',
            field=models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
