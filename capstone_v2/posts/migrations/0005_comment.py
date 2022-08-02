# Generated by Django 4.0.6 on 2022-08-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ManyToManyField(related_name='comments', to='posts.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]