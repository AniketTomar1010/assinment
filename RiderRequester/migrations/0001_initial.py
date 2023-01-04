# Generated by Django 3.2.16 on 2023-01-04 18:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=180)),
                ('Phone', models.IntegerField(unique=True)),
                ('From_location', models.CharField(max_length=180)),
                ('To_location', models.CharField(max_length=180)),
                ('Number_of_assets', models.IntegerField(default=0)),
                ('Type_of_assets', models.CharField(max_length=180)),
                ('Sensitivities', models.CharField(max_length=180)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestFromRequester',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=180)),
                ('sensitivities', models.CharField(max_length=180)),
                ('Number_of_people', models.IntegerField(default=0)),
                ('Status', models.CharField(default='Pending', max_length=180)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=180)),
                ('Medium', models.CharField(max_length=180)),
                ('From_location', models.CharField(max_length=180)),
                ('To_location', models.CharField(max_length=180)),
                ('number_of_assets', models.IntegerField(default=0)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterRider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Requester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RiderRequester.requester')),
                ('Rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RiderRequester.rider')),
            ],
        ),
    ]