# Generated by Django 3.2.16 on 2023-01-04 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RiderRequester', '0002_requester_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RequestFromRequester',
        ),
        migrations.AlterField(
            model_name='registerrider',
            name='Requester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RiderRequester.requester', unique=True),
        ),
        migrations.AlterField(
            model_name='registerrider',
            name='Rider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RiderRequester.rider', unique=True),
        ),
    ]
