# Generated by Django 3.1.7 on 2021-04-06 16:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.RemoveField(
            model_name='historicalaccount',
            name='id',
        ),
        migrations.AddField(
            model_name='account',
            name='account_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='account_no',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
