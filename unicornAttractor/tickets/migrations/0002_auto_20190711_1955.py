# Generated by Django 2.2.3 on 2019-07-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='DateTimeCreated',
            new_name='dateTimeCreated',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='LastUpdatedDateTime',
            new_name='lastUpdatedDateTime',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='LastUpdatedByID',
        ),
        migrations.AddField(
            model_name='ticket',
            name='lastUpdatedByID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='userID',
            field=models.IntegerField(default=0),
        ),
    ]
