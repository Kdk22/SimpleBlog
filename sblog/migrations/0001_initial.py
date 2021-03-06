# Generated by Django 2.2 on 2019-04-14 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('categories', models.CharField(max_length=300)),
                ('comment_count', models.IntegerField(null=True)),
                ('like_count', models.IntegerField(null=True)),
                ('icon', models.FileField(upload_to='')),
                ('post_date', models.DateTimeField(verbose_name='posted Date')),
                ('update_date', models.DateTimeField(null=True, verbose_name='update Date')),
            ],
        ),
    ]
