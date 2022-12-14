# Generated by Django 4.0.6 on 2022-08-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_participant_meetup_partiants'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-04-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='hello@hello.com', max_length=254),
            preserve_default=False,
        ),
    ]
