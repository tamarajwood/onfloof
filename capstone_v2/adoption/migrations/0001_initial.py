# Generated by Django 4.0.6 on 2022-07-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('breed', models.CharField(max_length=100)),
                ('endurance', models.BooleanField(default=False)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['breed'],
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
                ('breed', models.ManyToManyField(related_name='breeds', to='adoption.breed')),
            ],
        ),
    ]