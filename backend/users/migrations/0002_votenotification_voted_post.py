# Generated by Django 3.1.8 on 2021-05-10 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votenotification',
            name='voted_post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
            preserve_default=False,
        ),
    ]
