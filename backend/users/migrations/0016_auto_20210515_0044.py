# Generated by Django 3.1.8 on 2021-05-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210515_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follownotification',
            name='status',
        ),
        migrations.RemoveField(
            model_name='votenotification',
            name='status',
        ),
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('read', 'Read'), ('unread', 'Unread')], default='unread', max_length=10),
        ),
    ]
